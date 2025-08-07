from crewai import Agent
from config import OPENAI_API_KEY

resume_analyzer = Agent(
    role="Resume Analyzer",
    goal="Extract and summarize key sections from a resume: skills, education, experience, and projects",
    backstory="You are an expert in resume parsing and talent evaluation. You read resumes and extract relevant technical and soft skills.",
    verbose=True,
    llm_config={
        "model": "gpt-3.5-turbo",  
        "api_key": OPENAI_API_KEY ,   
        "provider":  "openai"  
    }
)
