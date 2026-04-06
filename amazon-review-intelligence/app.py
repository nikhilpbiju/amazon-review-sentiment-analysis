import streamlit as st

from src.load_data import load_reviews
from src.roberta_sentiment import get_roberta_sentiment
from src.decision import detect_mismatch, final_verdict
from src.aspects import extract_pain_points

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="Amazon Review Intelligence",
    layout="centered"
)

st.title("🛒 Amazon Review Intelligence")
st.write(
    "Analyze real Amazon reviews using RoBERTa sentiment analysis "
    "and get actionable product insights."
)

# ---------------- CACHED PIPELINE ----------------
@st.cache_data(show_spinner=False)
def run_full_analysis(asin):
    df = load_reviews(asin=asin)

    if df.empty:
        return None

    MAX_REVIEWS = 300
    if len(df) > MAX_REVIEWS:
        df = df.sample(MAX_REVIEWS, random_state=42)

    df["sentiment"] = df["review"].apply(get_roberta_sentiment)
    df["mismatch"] = df.apply(detect_mismatch, axis=1)

    negative_reviews = df[df["sentiment"] < -0.05]["review"]
    pain_points = extract_pain_points(negative_reviews, top_n=5) if len(negative_reviews) > 0 else []

    verdict, neg_pct, mismatch_pct = final_verdict(df, pain_points)

    return df, pain_points, verdict, neg_pct, mismatch_pct

# ---------------- USER INPUT ----------------
asin = st.text_input("Enter Amazon Product ASIN")

# ---------------- MAIN ACTION ----------------
if st.button("Analyze"):

    with st.spinner("Running analysis (cached per product)..."):
        result = run_full_analysis(asin)

    if result is None:
        st.error("No reviews found for this ASIN.")
        st.stop()

    df, pain_points, verdict, neg_pct, mismatch_pct = result

    st.success(f"Analyzed {len(df)} reviews")

    # ---------------- VISUALS ----------------
    st.subheader("📊 Rating Distribution")
    st.bar_chart(df["rating"].value_counts())

    st.subheader("🙂 Sentiment Distribution")
    sentiment_labels = df["sentiment"].apply(
        lambda x: "Positive" if x > 0.05 else "Negative" if x < -0.05 else "Neutral"
    )
    st.bar_chart(sentiment_labels.value_counts())

    # ---------------- PAIN POINTS ----------------
    st.subheader("💥 Top Customer Pain Points")

    if pain_points:
        pain_df = [{"Issue": i, "Mentions": c} for i, c in pain_points]
        st.bar_chart({row["Issue"]: row["Mentions"] for row in pain_df})
        st.table(pain_df)
    else:
        st.info("No significant negative reviews detected.")

    # ---------------- INSIGHT SUMMARY ----------------
    st.subheader("🧠 Insight Summary")

    if pain_points:
        top_issues = ", ".join([i for i, _ in pain_points[:2]])
    else:
        top_issues = "no major recurring issues"

    if mismatch_pct > 20:
        rating_trust = "ratings show notable sentiment mismatch"
    else:
        rating_trust = "ratings generally align with review sentiment"

    if neg_pct > 30:
        usage_fit = "not recommended for long-term or heavy usage"
    elif neg_pct > 15:
        usage_fit = "best suited for casual or short-term use"
    else:
        usage_fit = "generally suitable for most users"

    st.markdown(
        f"Customer feedback indicates that the main sources of dissatisfaction are **{top_issues}**. "
        f"Approximately **{neg_pct:.2f}%** of reviews express negative sentiment. "
        f"Additionally, **{mismatch_pct:.2f}%** of reviews show rating–sentiment mismatch, "
        f"suggesting that {rating_trust}. Overall, this product is **{usage_fit}**."
    )

    # ---------------- FINAL VERDICT ----------------
    st.subheader("🧠 Final Recommendation")

    col1, col2 = st.columns(2)
    col1.metric("Negative Review %", f"{neg_pct:.2f}%")
    col2.metric("Mismatch %", f"{mismatch_pct:.2f}%")

    if "Don’t Buy" in verdict:
        st.error(verdict)
    elif "Caution" in verdict:
        st.warning(verdict)
    else:
        st.success(verdict)
