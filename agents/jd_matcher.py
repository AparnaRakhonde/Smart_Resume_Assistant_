from crewai import Agent
from config import OPENAI_API_KEY


jd_matcher = Agent(
    role="Job Description Matcher",
    goal="Compare the resume with a job description and identify matching and missing skills or requirements",
    backstory="You specialize in job market analysis and understand what employers look for in resumes. Your job is to match candidate skills and experiences to job requirements.",
    verbose=True,
    llm_config={
        "model": "gpt-3.5-turbo",  
        "api_key": OPENAI_API_KEY,   
        "provider":  "openai"  
    }
)
