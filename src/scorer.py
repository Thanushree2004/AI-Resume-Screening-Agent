def calculate_education_score(resume_education, required_education):
    """
    Calculate education match score.

    Returns a score between 0 and 100.
    """

    resume_text = resume_education.lower()
    required_text = required_education.lower()

    keywords = [
        "computer science",
        "information technology",
        "software engineering",
        "engineering",
        "bachelor",
        "b.e",
        "b.tech",
        "bca",
        "mca"
    ]

    matched_keywords = 0
    total_keywords = 0

    for keyword in keywords:
        if keyword in required_text:
            total_keywords += 1

            if keyword in resume_text:
                matched_keywords += 1

    if total_keywords == 0:
        return 0

    return round(
        (matched_keywords / total_keywords) * 100,
        2
    )


def calculate_experience_score(resume_experience, required_experience):
    """
    Calculate experience match score.

    Freshers are accepted because the sample JD
    explicitly allows freshers.
    """

    resume_text = resume_experience.lower()
    required_text = required_experience.lower()

    if "fresher" in required_text:
        if "fresher" in resume_text or "internship" in resume_text:
            return 100

    if "0-2" in required_text:
        if "fresher" in resume_text or "internship" in resume_text:
            return 100

    if resume_text == "not found":
        return 0

    return 50


def calculate_project_score(resume_projects, job_description):
    """
    Calculate project relevance using simple keyword overlap.
    """

    resume_words = set(
        word.lower().strip(".,()")
        for word in resume_projects.split()
        if len(word) > 2
    )

    jd_words = set(
        word.lower().strip(".,()")
        for word in job_description.split()
        if len(word) > 2
    )

    if not resume_words or not jd_words:
        return 0

    overlap = resume_words.intersection(jd_words)

    score = (
        len(overlap) /
        len(jd_words)
    ) * 100

    return round(min(score * 5, 100), 2)


def calculate_final_score(
    skill_match_score,
    nlp_similarity_score,
    education_score,
    experience_score,
    project_score
):
    """
    Calculate the final candidate score.

    Weighting:
    Skills       = 50%
    NLP          = 20%
    Education    = 15%
    Experience   = 10%
    Projects     = 5%
    """

    final_score = (
        skill_match_score * 0.50
        + nlp_similarity_score * 0.20
        + education_score * 0.15
        + experience_score * 0.10
        + project_score * 0.05
    )

    return round(final_score, 2)