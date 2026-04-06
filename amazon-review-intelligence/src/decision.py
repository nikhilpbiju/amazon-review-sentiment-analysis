def detect_mismatch(row):
    rating = row["rating"]
    sentiment = row["sentiment"]

    if rating >= 4 and sentiment < -0.05:
        return "Positive Rating / Negative Sentiment"

    if rating <= 2 and sentiment > 0.05:
        return "Negative Rating / Positive Sentiment"

    return "Aligned"

def final_verdict(df, pain_points):
    total = len(df)
    negative_pct = len(df[df["sentiment"] < -0.05]) / total * 100
    mismatch_pct = len(df[df["mismatch"] != "Aligned"]) / total * 100

    core_issues = {"comfort", "quality", "battery", "durability", "sound"}
    dominant_core_issue = any(
        issue in core_issues for issue, _ in pain_points[:3]
    )

    if negative_pct > 35 or (mismatch_pct > 25 and dominant_core_issue):
        return "❌ Don’t Buy", negative_pct, mismatch_pct

    if negative_pct > 20 or mismatch_pct > 15:
        return "⚠️ Buy with Caution", negative_pct, mismatch_pct

    return "✅ Buy", negative_pct, mismatch_pct
