# RAG Career Coach - ATS 100/100 Scorer

An AI-powered RAG application built for TechX Solutions JD to analyze resumes and provide ATS scores with detailed breakdown.

### 🚀 Problem Solved
Most resume parsers fail on scanned / image-based PDFs and return `0 characters`.
**Solution:** Implemented hybrid pipeline using **PyMuPDF + Pytesseract OCR (300 DPI)** to extract text from both digital and scanned PDFs.

### 💡 Key Features
- ATS Score out of 100 against JD
- Smart Breakdown Table for matched/missing keywords
- OCR Support for image PDFs
- LLM Powered with Groq Llama 3

### 🛠️ Tech Stack
Python, Streamlit, Groq (Llama 3), LangChain, FAISS, Hugging Face Transformers, RAG, Prompt Engineering, PyMuPDF, Pytesseract OCR

### 📊 Result
My own resume scores 100/100 for TechX AI Intern (LLM & GenAI) role.

### How to Run
pip install -r requirements.txt
streamlit run app.py
