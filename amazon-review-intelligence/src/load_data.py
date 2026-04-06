import pandas as pd

def load_reviews(
    path="/Users/nikhil/Documents/amazon reviews analysis/amazon-review-intelligence/data/Reviews.csv",
    asin=None,
    sample_size=1000
):
    df = pd.read_csv(path)

    df = df[["ProductId", "Score", "Text"]]
    df.columns = ["asin", "rating", "review"]
    df = df.dropna()

    if asin:
        df = df[df["asin"] == asin]

    if len(df) == 0:
        return df

    if len(df) > sample_size:
        df = df.sample(sample_size, random_state=42)

    return df
