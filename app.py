import streamlit as st
import fitz
import re

st.set_page_config(page_title="RAG Career Coach")
st.title("🚀 RAG Career Coach - ATS Scorer")

jd = st.sidebar.text_area("JD paste karo", value="Python, Pandas, Scikit-Learn, OpenAI, Groq, RAG, LangChain, Streamlit")

def get_text(pdf):
    doc = fitz.open(stream=pdf.read(), filetype="pdf")
    text = ""
    for p in doc:
        text += p.get_text() + "\n"
    return text

file = st.file_uploader("Resume PDF", type="pdf")
if file:
    txt = get_text(file)
    st.success(f"Text mil gaya: {len(txt)} chars")
    kws = set([k.lower() for k in re.split(r'[, \n]+', jd) if k])
    matched = [k for k in kws if k in txt.lower()]
    score = int(len(matched)/len(kws)*100) if kws else 0
    st.metric("ATS Score", f"{score}/100")
    st.write("Matched:", ", ".join(matched))

   
           
