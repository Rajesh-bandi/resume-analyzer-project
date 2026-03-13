def generate_summary(skills):

    if len(skills) == 0:
        return "No major skills detected in the resume."

    summary = "This candidate has experience in "

    summary += ", ".join(skills)

    summary += "."

    return summary