# 🤖 Smart Resume Assistant

Hi there! I’m **Aparna Ganesh Rakhonde**, a job seeker just like you — and I built this AI-powered assistant to help **improve resumes and boost job applications**.

**Smart Resume Assistant** reads your resume, compares it with a job description, and gives you clear, useful feedback. Whether you're applying for your first job, an internship, or making a career move — this tool helps you **stand out**.

---

## 🚀 What This Tool Does

🔍 **Analyzes Your Resume**  
Pulls out your skills, education, projects, and work experience.

🤝 **Matches You to the Job**  
Compares your resume with the job description and shows how well they align.

📉 **Finds Skill Gaps**  
Tells you what skills or experiences you're missing — and what you can work on.

✍️ **Rewrites Key Sections**  
Improves your resume summary and experience to better match the job — while keeping your voice and tone.

---

## 👥 Who Is This For?

✅ Job Seekers  
✅ Students & Interns  
✅ Career Changers  
✅ Freshers & Entry-Level Applicants  
✅ Anyone wanting a smarter, AI-powered resume check!

---

## 💻 How to Use It (Don’t worry — it’s easy!)

### 1. Install the Requirements

Make sure Python is installed, then open a terminal and run:

```bash
pip install -r requirements.txt
```

### 2. Add Your OpenAI API Key

Create a `.env` file and paste your API key like this:

```ini
OPENAI_API_KEY=your_openai_api_key_here
```

(You can get your API key from [OpenAI](https://platform.openai.com/account/api-keys))

### 3. Run the App

```bash
streamlit run streamlit_app.py
```

The app will open in your browser. Just upload your **resume (PDF)** and paste the **job description** — the assistant will take it from there!

---

## 📦 What’s Inside

- `streamlit_app.py` – The Streamlit web app  
- `main.py` – The engine that runs all the AI tasks  
- `agents/` – AI agents:
  - Resume Analyzer  
  - Job Description Matcher  
  - Skill Gap Finder  
  - Resume Rewriter  
- `utils/file_parser.py` – Extracts text from your resume  
- `config.py` – Loads your OpenAI API key  
- `requirements.txt` – List of packages needed to run the app  

---

## 💡 Why I Built This

As a job seeker, I kept asking myself:

> "Is my resume good enough?"  
> "Am I missing important skills?"  
> "How can I tailor my resume quickly?"

So I built **Smart Resume Assistant** — a tool that helps me and others **prepare better, faster, and smarter**.

---

## 🔧 Tech Stack

- 🧠 **OpenAI GPT-3.5** – to understand and improve resume content  
- 🤖 **CrewAI** – to run multiple agents with specific tasks  
- 🌐 **Streamlit** – for the user interface  
- 📄 **PyPDF2 & PyMuPDF** – to read resumes from PDF files  

---

## 👩‍💻 Created By

**Aparna Ganesh Rakhonde**  
Completed Internship @ Tata Motors Passenger Vehicles Limited | AI + NLP Enthusiast | Aspiring ML Engineer  

---
