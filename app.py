import streamlit as st
from pdfminer.high_level import extract_text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import os

# Download necessary NLTK data (for Streamlit Cloud)
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as f:
        text = extract_text(f)
    return text

# Function to clean and tokenize the text
def clean_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered = [w for w in words if w.lower() not in stop_words and w.isalpha()]
    return filtered

# Streamlit App UI
st.title("📄 Resume Parser")
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    raw_text = extract_text_from_pdf("temp_resume.pdf")
    tokens = clean_text(raw_text)

    st.subheader("Extracted Text:")
    st.write(raw_text)

    st.subheader("Cleaned Tokens (No stopwords):")
    st.write(tokens)

    os.remove("temp_resume.pdf")



