def extract_skills(resume_text, skills_file):

    with open(skills_file, "r") as file:
        skills_list = file.read().splitlines()

    resume_text = resume_text.lower()

    found_skills = []

    for skill in skills_list:
        if skill.lower() in resume_text:
            found_skills.append(skill)

    return found_skills