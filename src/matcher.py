from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_text_similarity(resume_text, job_description_text):
    """
    Calculate similarity between a resume and a job description
    using TF-IDF and cosine similarity.

    Returns a score between 0 and 100.
    """

    documents = [
        resume_text,
        job_description_text
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def calculate_skill_match(resume_skills, required_skills):
    """
    Compare resume skills with required job skills.

    Returns:
        matched skills
        missing skills
        skill match percentage
    """

    resume_skill_set = {
        skill.strip().lower()
        for skill in resume_skills.split(",")
        if skill.strip()
    }

    required_skill_set = {
        skill.strip().lower()
        for skill in required_skills.splitlines()
        if skill.strip()
    }

    matched_skills = sorted(
        resume_skill_set.intersection(required_skill_set)
    )

    missing_skills = sorted(
        required_skill_set.difference(resume_skill_set)
    )

    if required_skill_set:
        match_percentage = (
            len(matched_skills) /
            len(required_skill_set)
        ) * 100
    else:
        match_percentage = 0

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(match_percentage, 2)
    }