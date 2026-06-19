import streamlit as st
from detector import analyze_news
from groq_explainer import get_explanation

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="🔍",
    layout="centered"
)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🔍 Fake News Detector for Students")
st.markdown("Paste any **news headline or article** below and AI will check its credibility instantly.")
st.divider()

# ── Input ─────────────────────────────────────────────────────────────────────
article = st.text_area(
    label="📰 News Article / Headline",
    placeholder="Paste your news article or headline here...",
    height=200
)

use_groq = st.checkbox("💬 Also get AI explanation (requires Groq API key in secrets)", value=False)

analyze_btn = st.button("🔎 Analyze Now", type="primary", use_container_width=True)

# ── Analysis ──────────────────────────────────────────────────────────────────
if analyze_btn:
    if not article.strip():
        st.warning("⚠️ Please paste some news text first.")
    elif len(article.strip()) < 20:
        st.warning("⚠️ Please enter at least a full headline (20+ characters).")
    else:
        with st.spinner("🤖 Analyzing with AI..."):
            label, score = analyze_news(article)

        # ── Result card ───────────────────────────────────────────────────────
        st.divider()
        col1, col2 = st.columns([1, 2])

        with col1:
            if label == "FAKE":
                st.error("🚨 FAKE NEWS")
            elif label == "REAL":
                st.success("✅ REAL NEWS")
            else:
                st.warning("⚠️ UNCERTAIN")

        with col2:
            st.metric("Confidence Score", f"{score:.1f}%")
            st.progress(score / 100)

        # ── Interpretation ────────────────────────────────────────────────────
        st.markdown("### 📊 What does this mean?")
        if label == "FAKE" and score > 75:
            st.error("🔴 **High confidence this is fake.** Avoid sharing this article.")
        elif label == "FAKE" and score <= 75:
            st.warning("🟠 **Likely fake**, but confidence is moderate. Cross-check with trusted sources.")
        elif label == "REAL" and score > 75:
            st.success("🟢 **High confidence this is real.** The article shows credible language patterns.")
        elif label == "REAL" and score <= 75:
            st.info("🔵 **Likely real**, but always verify from multiple sources.")
        else:
            st.info("🟡 **Uncertain.** The model couldn't clearly classify this. Check manually.")

        # ── Groq Explanation ──────────────────────────────────────────────────
        if use_groq:
            st.divider()
            st.markdown("### 🤖 AI Explanation (Groq LLaMA-3)")
            with st.spinner("Getting detailed explanation..."):
                explanation = get_explanation(article, label, score)
            st.info(explanation)

        # ── Disclaimer ────────────────────────────────────────────────────────
        st.divider()
        st.caption(
            "⚠️ **Disclaimer:** This tool detects linguistic patterns of fake news using AI. "
            "It cannot verify real-world facts. Always cross-check important news with "
            "trusted sources like Reuters, BBC, or AP News."
        )
