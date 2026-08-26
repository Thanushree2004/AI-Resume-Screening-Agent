import re


def normalize_text(text):
    """Normalize text for comparison."""
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\- ]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def calculate_education_score(
    resume_education,
    required_education
):
    """
    Calculate education compatibility.

    A direct degree/field match receives a high score.
    Related engineering/computer degrees receive partial credit.
    """

    resume = normalize_text(resume_education)
    required = normalize_text(required_education)

    if not resume or resume == "not found":
        return 0.0

    # Strong field matches
    strong_matches = [
        "computer science",
        "information technology",
        "software engineering",
        "computer applications"
    ]

    # Related degrees
    related_matches = [
        "engineering",
        "bachelor",
        "b.e",
        "b.tech",
        "bca",
        "mca"
    ]

    strong_match = any(
        keyword in resume
        for keyword in strong_matches
        if keyword in required
    )

    if strong_match:
        return 100.0

    related_match = any(
        keyword in resume
        for keyword in related_matches
        if keyword in required
    )

    if related_match:
        return 75.0

    # General bachelor's degree compatibility
    if "bachelor" in resume and "bachelor" in required:
        return 70.0

    return 40.0


def calculate_experience_score(
    resume_experience,
    required_experience
):
    """
    Calculate experience compatibility.

    Freshers are accepted when the JD explicitly allows them.
    """

    resume = normalize_text(resume_experience)
    required = normalize_text(required_experience)

    if not resume or resume == "not found":
        return 0.0

    fresher_allowed = (
        "fresher" in required
        or "0-2" in required
        or "0 2" in required
        or "freshers" in required
    )

    candidate_is_fresher = (
        "fresher" in resume
        or "internship" in resume
    )

    if fresher_allowed and candidate_is_fresher:
        return 100.0

    if "year" in resume and "year" in required:
        return 100.0

    if candidate_is_fresher:
        return 75.0

    return 50.0


def calculate_project_score(
    resume_projects,
    job_description
):
    """
    Calculate project relevance using meaningful technical
    keyword overlap rather than raw word overlap.
    """

    resume = normalize_text(resume_projects)
    jd = normalize_text(job_description)

    if (
        not resume
        or resume == "not found"
        or not jd
    ):
        return 0.0

    technical_keywords = [
        "python",
        "sql",
        "flask",
        "django",
        "rest",
        "api",
        "git",
        "javascript",
        "html",
        "css",
        "linux",
        "docker",
        "aws",
        "machine learning",
        "database",
        "software",
        "development",
        "testing",
        "debug"
    ]

    required_keywords = [
        keyword
        for keyword in technical_keywords
        if keyword in jd
    ]

    if not required_keywords:
        return 0.0

    matched = [
        keyword
        for keyword in required_keywords
        if keyword in resume
    ]

    score = (
        len(matched)
        / len(required_keywords)
    ) * 100

    return round(score, 2)


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
        Required skills = 50%
        NLP similarity  = 20%
        Education       = 15%
        Experience      = 10%
        Projects        = 5%
    """

    final_score = (
        skill_match_score * 0.50
        + nlp_similarity_score * 0.20
        + education_score * 0.15
        + experience_score * 0.10
        + project_score * 0.05
    )

    return round(
        min(max(final_score, 0), 100),
        2
    )