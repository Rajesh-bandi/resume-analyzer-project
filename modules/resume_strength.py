def calculate_resume_strength(resume_text, resume_skills):

    score = 0

    if "project" in resume_text.lower():
        score += 20

    if "experience" in resume_text.lower():
        score += 20

    if "certification" in resume_text.lower():
        score += 20

    if len(resume_skills) > 5:
        score += 20

    score += 20

    return score