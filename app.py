import streamlit as st
from groq import Groq
import fitz  # PyMuPDF
from PIL import Image
import pytesseract

# یہ لائن سب سے اہم ہے - اس سے ایرر ختم ہوگا
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.set_page_config(page_title="RAG Career Coach Pro")
st.title("🤖 AI Career Coach - Auto OCR")

api_key = st.text_input("Groq API Key", type="password")
resume_file = st.file_uploader("Resume PDF اپلوڈ کریں", type="pdf")
jd_file = st.file_uploader("JD PDF اپلوڈ کریں", type="pdf")
question = st.text_input("سوال", value="Give ATS score out of 100, list missing skills and keywords. Answer in English only.")

def extract_text_pro(pdf_file):
    pdf_file.seek(0)
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    
    # اگر ٹیکسٹ نہ ملے تو OCR لگاؤ
    if len(text.strip()) < 50:
        st.warning("یہ Image والی PDF ہے، اب OCR سے پڑھ رہا ہوں...")
        pdf_file.seek(0)
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        ocr_text = ""
        for page in doc:
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            ocr_text += pytesseract.image_to_string(img) + "\n"
        text = ocr_text
    return text

if st.button("Ask AI 🚀", type="primary"):
    if not api_key or not resume_file or not jd_file:
        st.error("پہلے Key اور دونوں PDFs لگائیں")
    else:
        with st.spinner("PDF پڑھ رہا ہوں..."):
            r_text = extract_text_pro(resume_file)
            j_text = extract_text_pro(jd_file)

            st.write(f"Resume: {len(r_text)} characters | JD: {len(j_text)} characters")

            client = Groq(api_key=api_key)
            prompt = f"RESUME: {r_text[:6000]}\n\nJD: {j_text[:6000]}\n\nTASK: {question}. Use the provided text, do not ask for documents again."
            
            res = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {"role":"system", "content":"You are a career coach. Answer in English only."},
                    {"role":"user", "content": prompt}
                ]
            )
            st.success("ATS Analysis:")
            st.write(res.choices[0].message.content)
