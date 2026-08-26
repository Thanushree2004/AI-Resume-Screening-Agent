import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def generate_rule_based_reasoning(candidate):
    """
    Generate transparent reasoning without using an LLM.
    """

    score = candidate["final_score"]
    skill_score = candidate["skill_score"]
    education_score = candidate["education_score"]
    experience_score = candidate["experience_score"]
    project_score = candidate["project_score"]

    matched = candidate["matched_skills"]
    missing = candidate["missing_skills"]

    # Overall assessment
    if score >= 80:
        assessment = (
            "The candidate is a strong match for the "
            "Junior Python Developer role."
        )
        recommendation = (
            "Recommended for the next stage of the "
            "selection process."
        )

    elif score >= 65:
        assessment = (
            "The candidate is a good match for the "
            "Junior Python Developer role."
        )
        recommendation = (
            "Consider the candidate for the next stage "
            "with additional technical evaluation."
        )

    elif score >= 50:
        assessment = (
            "The candidate is a moderate match for the "
            "Junior Python Developer role."
        )
        recommendation = (
            "Consider only after evaluating the candidate's "
            "technical gaps."
        )

    else:
        assessment = (
            "The candidate has limited alignment with the "
            "Junior Python Developer role."
        )
        recommendation = (
            "Not recommended for the next stage based "
            "on the current screening criteria."
        )

    # Strengths
    strengths = []

    if skill_score >= 75:
        strengths.append(
            f"Strong required-skill match ({skill_score}%)."
        )
    elif skill_score >= 50:
        strengths.append(
            f"Moderate required-skill match ({skill_score}%)."
        )

    if education_score >= 75:
        strengths.append(
            "Education background aligns with the role."
        )

    if experience_score >= 75:
        strengths.append(
            "Experience level aligns with the job requirements."
        )

    if project_score >= 50:
        strengths.append(
            "Projects show relevant technical alignment."
        )

    if matched:
        strengths.append(
            f"Matched skills: {matched}."
        )

    if not strengths:
        strengths.append(
            "Limited strengths were identified by the "
            "current screening rules."
        )

    # Weak areas
    weak_areas = []

    if missing:
        weak_areas.append(
            f"Missing required skills: {missing}."
        )

    if skill_score < 50:
        weak_areas.append(
            "Required-skill coverage is below 50%."
        )

    if education_score < 75:
        weak_areas.append(
            "Education match is not strong."
        )

    if experience_score < 75:
        weak_areas.append(
            "Experience alignment is limited."
        )

    if project_score < 50:
        weak_areas.append(
            "Project relevance is limited."
        )

    if not weak_areas:
        weak_areas.append(
            "No major weaknesses were identified "
            "by the screening rules."
        )

    reasoning = f"""
Overall Assessment:
{assessment}

Key Strengths:
- {" ".join(strengths)}

Missing or Weak Areas:
- {" ".join(weak_areas)}

Why This Score:
The final score of {score}/100 is based on the weighted
combination of required skill match ({skill_score}%),
NLP similarity ({candidate["nlp_score"]}%),
education match ({education_score}%),
experience match ({experience_score}%),
and project relevance ({project_score}%).

Recommendation:
{recommendation}
"""

    return reasoning.strip()


def generate_candidate_reasoning(candidate, job_description):
    """
    Generate AI reasoning when API access is available.

    If the API is unavailable because of quota or another
    API problem, use transparent rule-based reasoning.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return (
            generate_rule_based_reasoning(candidate),
            "rule-based"
        )

    try:

        client = OpenAI(api_key=api_key)

        prompt = f"""
You are an AI recruitment assistant.

Evaluate this candidate against the provided job description.

JOB DESCRIPTION:
{job_description}

CANDIDATE:
Name: {candidate["name"]}
Email: {candidate["email"]}

Final Score: {candidate["final_score"]}/100
Skill Match: {candidate["skill_score"]}%
NLP Similarity: {candidate["nlp_score"]}%
Education Match: {candidate["education_score"]}%
Experience Match: {candidate["experience_score"]}%
Project Relevance: {candidate["project_score"]}%

Matched Skills:
{candidate["matched_skills"]}

Missing Skills:
{candidate["missing_skills"]}

Provide exactly these sections:

Overall Assessment:
Key Strengths:
Missing or Weak Areas:
Why This Score:
Recommendation:

Rules:
- Use only the information provided.
- Do not invent experience or skills.
- Clearly identify missing skills.
- Keep the assessment concise.
"""

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        return response.output_text.strip(), "llm"

    except Exception as error:

        error_text = str(error).lower()

        if (
            "quota" in error_text
            or "insufficient_quota" in error_text
            or "429" in error_text
        ):
            return (
                generate_rule_based_reasoning(candidate),
                "rule-based-fallback"
            )

        return (
            generate_rule_based_reasoning(candidate),
            "rule-based-fallback"
        )