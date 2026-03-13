import os

from modules.resume_parser import parse_resume
from modules.skill_extractor import extract_skills
from modules.ats_score import calculate_ats_score
from modules.resume_summary import generate_summary
from modules.skill_gap import skill_gap_analysis
from modules.resume_strength import calculate_resume_strength
from modules.role_predictor import predict_role


resume_file = "uploads/sample_resume.pdf"

job_description = """
Looking for a Data Scientist with skills in Python, SQL,
Machine Learning, Data Analysis and Pandas.
"""


# File validation
if not os.path.exists(resume_file):
    print("Resume file not found")
    exit()

if os.path.getsize(resume_file) > 600*1024:
    print("File size should be less than 600KB")
    exit()

if not resume_file.endswith((".pdf",".docx")):
    print("Only PDF or DOCX allowed")
    exit()


# Extract resume text
resume_text = parse_resume(resume_file)


# Extract skills
resume_skills = extract_skills(resume_text,"dataset/skills.txt")
job_skills = extract_skills(job_description,"dataset/skills.txt")


# ATS score
ats_score = calculate_ats_score(resume_text,job_description)


# Summary
summary = generate_summary(resume_skills)


# Skill gap
matched,missing = skill_gap_analysis(resume_skills,job_skills)


# Resume strength
strength = calculate_resume_strength(resume_text,resume_skills)


# Role prediction
role = predict_role(resume_skills)


print("Detected Skills:",resume_skills)
print("ATS Score:",ats_score)
print("Matched Skills:",matched)
print("Missing Skills:",missing)
print("Resume Strength Score:",strength)
print("Recommended Role:",role)
print("Summary:",summary)