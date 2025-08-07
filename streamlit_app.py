# streamlit_app.py
import streamlit as st
import PyPDF2
from main import run_resume_analysis

st.set_page_config(page_title="Resume Insight Agent", layout="wide")
st.title("📄 Resume Insight Agent (Agentic AI)")

# Upload Resume PDF
st.subheader("Upload Your Resume (PDF)")
resume_file = st.file_uploader("Choose a PDF file", type="pdf")

# Job Description Input
st.subheader("Paste the Job Description")
job_desc = st.text_area("Job Description", height=200)

# Submit button
if st.button("🔍 Analyze Resume"):

    if resume_file is not None and job_desc.strip():
        # Extract text from PDF
        pdf_reader = PyPDF2.PdfReader(resume_file)
        resume_text = ""
        for page in pdf_reader.pages:
            resume_text += page.extract_text()

        with st.spinner("Running analysis..."):
            outputs = run_resume_analysis(resume_text, job_desc)

        # Display results
        st.subheader("📝 Analysis Results")
        task_names = [
            "Resume Summary",
            "JD Match Report",
            "Skill Gap Analysis",
            "Rewritten Resume"
        ]
        for title, output in zip(task_names, outputs):
            st.markdown(f"### 🔹 {title}")
            st.write(output)

    else:
        st.warning("Please upload a resume and provide a job description.")
