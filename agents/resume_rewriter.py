from crewai import Agent
from config import OPENAI_API_KEY


resume_rewriter = Agent(
    role="Resume Rewriter",
    goal="Rewrite the resume summary or description to match the job description while keeping it professional and authentic",
    backstory=(
        "You are a resume writing expert. Your goal is to improve resumes by rewriting the summary and experience section "
        "to better match the job requirements while keeping the candidate's voice and honesty intact."
    ),
    verbose=True,
    llm_config={
        "model": "gpt-3.5-turbo",  
        "api_key": OPENAI_API_KEY,   
        "provider":  "openai"  
    }
) 
