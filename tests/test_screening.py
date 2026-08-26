from src.matcher import (
    calculate_text_similarity,
    calculate_skill_match
)

from src.scorer import (
    calculate_education_score,
    calculate_experience_score,
    calculate_project_score,
    calculate_final_score
)

from src.ranker import rank_candidates


def test_text_similarity():

    score = calculate_text_similarity(
        "Python SQL Flask",
        "Python SQL Flask"
    )

    assert score > 90


def test_skill_matching():

    result = calculate_skill_match(
        "Python, SQL, Flask",
        "Python\nSQL\nFlask\nDjango"
    )

    assert result["match_percentage"] == 75.0

    assert "python" in result["matched_skills"]

    assert "django" in result["missing_skills"]


def test_education_matching():

    score = calculate_education_score(
        "Bachelor of Engineering in Computer Science",
        "Bachelor's degree in Computer Science"
    )

    assert score == 100.0


def test_fresher_experience():

    score = calculate_experience_score(
        "Fresher with internship experience",
        "0-2 years. Freshers can apply."
    )

    assert score == 100.0


def test_project_matching():

    score = calculate_project_score(
        "Developed a Python Flask REST API with SQL",
        "Python SQL Flask REST API"
    )

    assert score > 0


def test_final_score_range():

    score = calculate_final_score(
        80,
        60,
        100,
        100,
        80
    )

    assert 0 <= score <= 100


def test_candidate_ranking():

    candidates = [
        {
            "name": "Candidate A",
            "final_score": 60
        },
        {
            "name": "Candidate B",
            "final_score": 90
        },
        {
            "name": "Candidate C",
            "final_score": 75
        }
    ]

    ranked = rank_candidates(
        candidates
    )

    assert ranked[0]["name"] == "Candidate B"
    assert ranked[1]["name"] == "Candidate C"
    assert ranked[2]["name"] == "Candidate A"

    assert ranked[0]["rank"] == 1