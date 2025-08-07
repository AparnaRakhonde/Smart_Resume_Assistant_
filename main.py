import config
from crewai import Crew, Task
from agents.resume_analyzer import resume_analyzer
from agents.jd_matcher import jd_matcher
from agents.skill_gap_finder import skill_gap_finder
from agents.resume_rewriter import resume_rewriter

def run_resume_analysis(resume_text, job_desc):
    tasks = [
        Task(
            name="Resume Analysis",
            description="Analyze the resume and extract key sections like skills, education, experience, and projects.",
            expected_output="Structured summary of the resume.",
            agent=resume_analyzer,
        ),
        Task(
            name="JD Match Analysis",
            description="Compare the resume with the job description.",
            expected_output="Match percentage and explanation.",
            agent=jd_matcher,
        ),
        Task(
            name="Skill Gap Report",
            description="Find skill gaps between resume and job description.",
            expected_output="List of missing skills with learning suggestions.",
            agent=skill_gap_finder,
        ),
        Task(
            name="Rewritten Resume",
            description="Rewrite the resume to match job description better.",
            expected_output="Improved resume tailored to job description.",
            agent=resume_rewriter,
        ),
    ]

    crew = Crew(
        agents=[resume_analyzer, jd_matcher, skill_gap_finder, resume_rewriter],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff(inputs={"resume_text": resume_text, "job_desc": job_desc})
    return result.tasks_output
