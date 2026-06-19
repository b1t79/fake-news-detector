"""
groq_explainer.py
-----------------
Optional explanation layer using Groq's free LLaMA-3 API.
Signs up free at: https://console.groq.com
Add your key to Streamlit secrets: GROQ_API_KEY = "your_key_here"
"""

import streamlit as st

def get_explanation(article: str, label: str, score: float) -> str:
    """
    Use Groq LLaMA-3 to generate a plain-English explanation
    of why the article was classified as REAL or FAKE.

    Parameters
    ----------
    article : str   - The news text
    label   : str   - "REAL", "FAKE", or "UNCERTAIN"
    score   : float - Confidence score (0-100)

    Returns
    -------
    str - Human-readable explanation
    """
    try:
        from groq import Groq
    except ImportError:
        return "❌ Groq library not installed. Run: pip install groq"

    # Get API key from Streamlit secrets
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except (KeyError, FileNotFoundError):
        return (
            "❌ Groq API key not found. "
            "Add GROQ_API_KEY to your Streamlit secrets file (.streamlit/secrets.toml)."
        )

    client = Groq(api_key=api_key)

    prompt = f"""You are a media literacy expert helping students understand fake news.

A news article was analyzed by an AI model and classified as: {label} (confidence: {score:.1f}%)

Article text:
\"\"\"{article[:1000]}\"\"\"

Please provide a SHORT explanation (3-4 sentences) covering:
1. What linguistic or factual patterns suggest this is {label}
2. One or two specific red flags OR trust signals you notice
3. A quick tip for the student on how to verify this themselves

Keep your response simple and educational. Do not repeat the verdict — just explain it.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.4
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Groq API error: {str(e)}"
