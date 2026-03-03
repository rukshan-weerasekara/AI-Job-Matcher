import streamlit as st
import io
import re
import nltk
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer

# Download NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
ps = PorterStemmer()

def clean_and_stem(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    words = nltk.word_tokenize(text)
    stemmed_words = [ps.stem(w) for w in words]
    return " ".join(stemmed_words)

def get_pdf_text(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# UI Design
st.set_page_config(page_title="AI Job Matcher", page_icon="🚀")
st.title("AI Job Matcher")
st.markdown(f"**Developed by Rukshan Weerasekara** | Creative Technologist")
st.markdown("---")

job_desc = st.text_area("Paste Job Description here:", height=200)
uploaded_file = st.file_uploader("Upload your CV (PDF)", type="pdf")

if st.button("Check Match Score"):
    if job_desc and uploaded_file:
        cv_text = get_pdf_text(uploaded_file)
        
        # Logic
        clean_jd = clean_and_stem(job_desc)
        clean_cv = clean_and_stem(cv_text)
        
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([clean_jd, clean_cv])
        score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100
        
        st.metric(label="Match Score", value=f"{score:.2f}%")
        
        # Key Words
        jd_words = set(re.sub(r'[^\w\s]', ' ', job_desc.lower()).split())
        cv_words = set(re.sub(r'[^\w\s]', ' ', cv_text.lower()).split())
        missing = [word for word in (jd_words - cv_words) if len(word) > 4]
        
        st.info(f"💡 Missing Keywords: {', '.join(missing[:15])}")
    else:
        st.error("Please provide both Job Description and CV.")
