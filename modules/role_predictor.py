def predict_role(resume_skills):

    data_science = ["python","machine learning","pandas"]
    data_analyst = ["sql","excel","tableau"]

    ds_score = len(set(resume_skills) & set(data_science))
    da_score = len(set(resume_skills) & set(data_analyst))

    if ds_score > da_score:
        return "Data Scientist"
    else:
        return "Data Analyst"