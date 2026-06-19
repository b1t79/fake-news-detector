# 🔍 Fake News Detector for Students
**Capstone Project | Dax Hareshbhai Patel | MIT ADT University | CSE**

An AI-powered web app that analyzes news articles and detects fake news using a
pre-trained RoBERTa NLP model from HuggingFace, with an optional Groq LLaMA-3 explanation layer.

---

## 📁 Project Structure
```
fake-news-detector/
├── app.py                  ← Main Streamlit web app (UI + flow)
├── detector.py             ← Core AI engine (HuggingFace RoBERTa model)
├── groq_explainer.py       ← Optional: Groq LLaMA-3 explanation layer
├── requirements.txt        ← Python dependencies
├── .streamlit/
│   └── secrets.toml        ← API keys (DO NOT push to GitHub)
└── README.md
```

---

## 🚀 STEP-BY-STEP IMPLEMENTATION GUIDE

### STEP 1 — Install Python
- Download Python 3.10+ from https://python.org
- During install on Windows: ✅ check "Add Python to PATH"
- Verify: open terminal and run `python --version`

---

### STEP 2 — Set Up Project Folder
```bash
# Create project folder
mkdir fake-news-detector
cd fake-news-detector

# Create a virtual environment (keeps packages isolated)
python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

---

### STEP 3 — Install Dependencies
```bash
pip install streamlit transformers torch groq
```
⚠️ `torch` is a large download (~800MB). This may take 5-10 minutes.

---

### STEP 4 — Copy Project Files
Copy these files into your `fake-news-detector/` folder:
- `app.py`
- `detector.py`
- `groq_explainer.py`
- `requirements.txt`

Create the secrets folder:
```bash
mkdir .streamlit
# Then create .streamlit/secrets.toml and add your Groq key
```

---

### STEP 5 — Get Your FREE Groq API Key (Optional but Recommended)
1. Go to https://console.groq.com
2. Sign up for free (no credit card)
3. Click "API Keys" → "Create API Key"
4. Copy the key and paste it into `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxx"
   ```

---

### STEP 6 — Run the App Locally
```bash
streamlit run app.py
```
This will open the app at http://localhost:8501 in your browser automatically.

**First run:** The AI model (~500MB) will download automatically from HuggingFace.
Subsequent runs are instant (model is cached).

---

### STEP 7 — Test the App
Try these sample inputs:

**Likely FAKE:**
> "Scientists discover that drinking bleach cures cancer! Government hiding the truth."

**Likely REAL:**
> "The Reserve Bank of India raised interest rates by 25 basis points in its latest monetary policy meeting, citing rising inflation concerns."

---

### STEP 8 — Deploy to the Internet (FREE)

#### A. Push to GitHub
```bash
git init
git add app.py detector.py groq_explainer.py requirements.txt
# DO NOT add .streamlit/secrets.toml to git
echo ".streamlit/secrets.toml" >> .gitignore
git add .gitignore
git commit -m "Initial commit - Fake News Detector"
git remote add origin https://github.com/YOUR_USERNAME/fake-news-detector.git
git push -u origin main
```

#### B. Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io
2. Sign in with your GitHub account
3. Click "New app" → select your repository
4. Set "Main file path" to `app.py`
5. Click "Advanced settings" → add your `GROQ_API_KEY` as a secret
6. Click "Deploy!" — your app will be live in ~2 minutes!

---

## 🧠 How the AI Works

```
User Input (news text)
        ↓
  Text Tokenization
  (AutoTokenizer splits text into word pieces)
        ↓
  RoBERTa Model Inference
  (300M parameter transformer model)
        ↓
  Softmax Output → [FAKE prob, REAL prob]
        ↓
  Confidence Score + Label
        ↓
  (Optional) Groq LLaMA-3 Explanation
        ↓
  Display Result in Streamlit UI
```

---

## 📊 Model Info
- **Model:** `hamzab/roberta-fake-news-classification`
- **Base:** RoBERTa (Robustly Optimized BERT Pretraining Approach)
- **Training Data:** WELFake dataset — 72,134 news articles (37,106 real + 35,028 fake)
- **Accuracy:** ~88% on test set
- **Source:** https://huggingface.co/hamzab/roberta-fake-news-classification

---

## ⚠️ Known Limitations
- Cannot verify real-world facts (no internet access)
- Works best on English language articles
- May struggle with very short headlines (< 10 words)
- Satire/parody news may be misclassified

---

## 📚 References
1. HuggingFace Model: huggingface.co/hamzab/roberta-fake-news-classification
2. Streamlit Docs: docs.streamlit.io
3. Groq API: console.groq.com/docs
4. WELFake Dataset: Verma et al. (2021), IEEE Transactions on Computational Social Systems
