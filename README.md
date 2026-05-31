# Amazon Review Intelligence 🛒

An end-to-end NLP-powered customer intelligence system that analyzes Amazon product reviews, identifies hidden customer dissatisfaction, extracts key product pain points, detects rating–sentiment mismatches, and generates actionable **Buy / Caution / Don't Buy** recommendations.

---

## Overview

Product ratings alone often fail to reveal the full customer experience. Many products maintain high star ratings despite recurring complaints regarding comfort, battery life, build quality, durability, or other critical aspects.

This project uses transformer-based Natural Language Processing (NLP) to convert unstructured review text into decision-ready insights.

The system analyzes Amazon reviews for a specific product and answers questions such as:

* What are customers complaining about?
* Do review sentiments align with ratings?
* Are there signs of rating inflation?
* What are the most common pain points?
* Should a customer buy this product?

---

## Features

### 🤖 RoBERTa-Based Sentiment Analysis

Utilizes a pre-trained RoBERTa transformer model to classify review sentiment with contextual understanding.

Unlike traditional lexicon-based approaches, RoBERTa can better interpret:

* Nuanced feedback
* Mixed opinions
* Contextual sentiment
* Product-specific complaints

---

### 🚨 Rating–Sentiment Mismatch Detection

Detects situations where:

* High ratings contain negative sentiment
* Low ratings contain positive sentiment

Example:

**5★ Review**

> "Battery died after two months but overall okay."

**Detected as:** Negative Sentiment

This helps uncover:

* Hidden dissatisfaction
* Rating inflation
* Unreliable product ratings

---

### 💥 Customer Pain Point Extraction

Extracts and aggregates recurring complaint categories from negative reviews.

Examples include:

| Pain Point | Example Keywords         |
| ---------- | ------------------------ |
| Battery    | battery, charging, power |
| Comfort    | ears, pain, fit, comfort |
| Sound      | audio, bass, volume      |
| Quality    | build, material, plastic |
| Delivery   | shipping, package        |
| Price      | price, value, cost       |
| Durability | broke, damage, broken    |

This transforms hundreds of reviews into a concise list of customer concerns.

---

### 🧠 Insight Summary Generation

Generates a human-readable summary explaining:

* Major customer complaints
* Review reliability
* Product suitability
* Overall customer satisfaction

Example:

> Customer feedback indicates that the main sources of dissatisfaction are comfort and battery performance. Approximately 24% of reviews express negative sentiment. Additionally, 18% of reviews show rating–sentiment mismatch, suggesting moderate rating inflation. Overall, the product is suitable for casual users but may not be ideal for long-term use.

---

### ✅ Automated Product Recommendation

The system generates one of three recommendations:

* ✅ Buy
* ⚠️ Buy with Caution
* ❌ Don't Buy

Recommendations are based on:

* Negative sentiment percentage
* Rating–sentiment mismatch percentage
* Dominant customer pain points

---

## System Architecture

```text
Amazon Reviews
       │
       ▼
Review Preprocessing
       │
       ▼
RoBERTa Sentiment Analysis
       │
       ▼
Rating–Sentiment Mismatch Detection
       │
       ▼
Pain Point Extraction
       │
       ▼
Insight Generation
       │
       ▼
Buy / Caution / Don't Buy Recommendation
       │
       ▼
Streamlit Web Application
```

---

## Tech Stack

### Programming Language

* Python

### Machine Learning & NLP

* Hugging Face Transformers
* RoBERTa
* Pandas
* NumPy

### Web Application

* Streamlit

### Data Processing

* Regular Expressions (Regex)
* Custom Aspect Extraction Pipeline

---

## Project Structure

```text
amazon-review-intelligence/
│
├── app.py
├── data/
│   └── reviews.csv
│
├── src/
│   ├── load_data.py
│   ├── roberta_sentiment.py
│   ├── aspects.py
│   └── decision.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/amazon-review-intelligence.git
cd amazon-review-intelligence
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## Example Output

### Product Analysis

* Negative Reviews: 23.4%
* Rating–Sentiment Mismatch: 17.8%
* Top Pain Points:

  * Comfort
  * Battery
  * Sound

### Insight Summary

> Most customer dissatisfaction stems from comfort and battery-related issues. While overall ratings remain positive, a notable percentage of reviews exhibit sentiment-rating mismatch, suggesting that ratings may not fully reflect user experience. The product is recommended for casual users but may not be suitable for heavy long-term usage.

### Recommendation

⚠️ Buy with Caution

---

## Future Improvements

* Multi-product comparison dashboard
* Aspect-level sentiment analysis
* Time-series sentiment tracking
* Review summarization using LLMs
* Browser extension for live Amazon product analysis
* Deployment on Streamlit Cloud

---

## Resume Highlights

This project demonstrates:

* Applied NLP using Transformer Models
* Sentiment Analysis on Real-World Data
* Customer Intelligence & Product Analytics
* Web Application Development
* End-to-End Machine Learning Deployment

---

## Author

**Nikhil P Biju**

National Institute of Technology Warangal

Open to opportunities in:

* Machine Learning
* Data Science
* Product Analytics
* Software Engineering
