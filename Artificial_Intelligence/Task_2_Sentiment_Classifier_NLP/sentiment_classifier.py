# Progree Artificial Intelligence — Task 2
# Intelligent Multi-Class NLP Text Sentiment Classifier

import os
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, f1_score

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.strip()

def run_sentiment_pipeline():
    dataset_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_sentiment_dataset.csv")
    df = pd.read_csv(dataset_path)
    df['cleaned_text'] = df['text'].apply(clean_text)

    X_train, X_test, y_train, y_test = train_test_split(
        df['cleaned_text'], df['sentiment'], test_size=0.25, random_state=42, stratify=df['sentiment']
    )

    vectorizer = TfidfVectorizer(stop_words='english', max_features=150)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(random_state=42)
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)
    print("Overall Weighted F1-Score:", f1_score(y_test, y_pred, average='weighted'))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    run_sentiment_pipeline()
