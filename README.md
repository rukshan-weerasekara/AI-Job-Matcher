# 🎯 AI Job Matcher 

An intelligent career optimization tool designed for creative technologists to bridge the gap between their experience and high-tier job requirements. This utility uses Natural Language Processing (NLP) to calculate the mathematical similarity between a CV and a Job Description.

## 🔗 Live Demo
Check out the live app here: [https://ai-job-matcher-in7fasukdz7gqcngkskien.streamlit.app/](https://ai-job-matcher-in7fasukdz7gqcngkskien.streamlit.app/)

## 🚀 Project Overview
In a competitive job market, understanding how Automated Tracking Systems (ATS) perceive your profile is critical. This tool provides an "AI-eye view" of your CV, helping you identify exactly what's missing to land your dream role.

### Key Features:
* **PDF Intelligence:** Seamlessly extracts and parses text from PDF resumes.
* **NLP-Driven Scoring:** Uses TF-IDF vectorization to determine how well your skills align with the job role.
* **Missing Keyword Analysis:** Identifies specific industry keywords (e.g., *Troubleshooting, Infrastructure, AD, DNS*) missing from your profile.
* **Advanced Preprocessing:** Includes **Stemming** and **Regular Expression (Regex)** cleaning to ensure word variants (e.g., *Animating* vs *Animation*) are matched correctly.
* **Interactive UI:** A clean, fast interface built with Streamlit for real-time career optimization.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **ML Framework:** Scikit-learn (TF-IDF & Cosine Similarity)
* **NLP Engine:** NLTK (Natural Language Toolkit)
* **Frontend:** Streamlit
* **File Processing:** PyPDF2

## 🧠 The Logic
The system processes data through a sophisticated NLP pipeline:

1.  **Text Extraction:** Converts PDF binary data into raw string format using `PyPDF2`.
2.  **Preprocessing & Stemming:** Normalizes text by removing punctuation using Regex and reducing words to their root form using the **Porter Stemmer** algorithm.

3.  **TF-IDF Vectorization:** Converts text into numerical vectors, weighing the importance of specific technical terms over common filler words.
4.  **Cosine Similarity:** Calculates the 'distance' between the Job Description vector and the CV vector to produce a precise percentage score.


---
Developed by **Rukshan Weerasekara** *Creative Technologist | 3D Animator | AI Developer*
