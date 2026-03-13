from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(resume_text, job_description):

    documents = [resume_text, job_description]

    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(matrix)[0][1]

    ats_score = round(similarity * 100, 2)

    return ats_score