from transformers import pipeline
import streamlit as st

MODEL_NAME = "hamzab/roberta-fake-news-classification"

@st.cache_resource(show_spinner="Loading AI model...")
def load_model():
    classifier = pipeline(
        "text-classification",
        model=MODEL_NAME,
        truncation=True,
        max_length=512
    )
    return classifier

def analyze_news(text: str):
    classifier = load_model()
    text = text.strip()
    result = classifier(text)[0]
    
    raw_label = result["label"].upper()
    confidence = result["score"] * 100

    label_map = {
        "TRUE": "REAL",
        "FALSE": "FAKE",
        "LABEL_0": "REAL",
        "LABEL_1": "FAKE",
        "FAKE": "FAKE",
        "REAL": "REAL",
    }
    label = label_map.get(raw_label, raw_label)

    if confidence < 55:
        label = "UNCERTAIN"

    return label, confidence