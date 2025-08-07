from crewai import Agent
from config import OPENAI_API_KEY


skill_gap_finder = Agent(
    role="Skill Gap Finder",
    goal="Identify missing technical and soft skills in the resume compared to the job description",
    backstory=(
        "You are a career coach and talent development expert. "
        "You help candidates identify gaps in their skills and suggest what they need to learn or improve "
        "in order to meet job requirements."
    ),
    llm_config={
        "model": "gpt-3.5-turbo",  
        "api_key": OPENAI_API_KEY ,   
        "provider":  "openai"  
    }
)
