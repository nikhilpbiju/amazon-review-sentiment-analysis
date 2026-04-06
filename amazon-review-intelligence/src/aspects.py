import re
from collections import Counter

# Lightweight stopword list (enough for reviews)
STOPWORDS = {
    "i", "me", "my", "we", "you", "it", "this", "that", "they",
    "is", "was", "are", "were", "be", "been",
    "the", "a", "an", "and", "or", "but",
    "to", "of", "in", "on", "for", "with", "as",
    "very", "so", "too", "also", "just",
    "product", "products", "item", "items"
}

# Domain-specific aspect mapping (THIS is the intelligence)
ASPECT_MAP = {
    "battery": {"battery", "charge", "charging", "power"},
    "comfort": {"comfort", "ear", "ears", "pain", "hurt", "fit"},
    "sound": {"sound", "audio", "bass", "noise", "volume"},
    "quality": {"quality", "build", "material", "plastic"},
    "delivery": {"delivery", "shipping", "package", "packaging"},
    "price": {"price", "cost", "value", "expensive", "cheap"},
    "durability": {"durability", "broke", "break", "broken", "damage"},
}

def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.split()

def extract_pain_points(reviews, top_n=10):
    aspect_counter = Counter()

    for review in reviews:
        tokens = tokenize(review)

        for token in tokens:
            if token in STOPWORDS or len(token) < 3:
                continue

            for aspect, keywords in ASPECT_MAP.items():
                if token in keywords:
                    aspect_counter[aspect] += 1

    return aspect_counter.most_common(top_n)
