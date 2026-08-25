import re


def clean_text(text):
    """Clean unnecessary spaces and blank lines."""
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n+", "\n", text)
    return text.strip()


def extract_name(text):
    """Extract the candidate name from the first non-empty line."""

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if lines:
        return lines[0]

    return "Not Found"


def extract_email(text):
    """Extract the candidate email address."""

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return "Not Found"


def extract_section(text, section_name, next_sections):
    """Extract content belonging to a resume section."""

    next_section_pattern = "|".join(
        re.escape(section)
        for section in next_sections
    )

    pattern = rf"{re.escape(section_name)}\s*(.*?)(?=\n(?:{next_section_pattern})\s*\n|\Z)"

    match = re.search(
        pattern,
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return "Not Found"


def extract_skills(text):
    """Extract the skills section."""

    next_sections = [
        "EDUCATION",
        "PROJECTS",
        "EXPERIENCE",
        "WORK EXPERIENCE",
        "INTERNSHIP",
        "CERTIFICATIONS"
    ]

    return extract_section(
        text,
        "SKILLS",
        next_sections
    )


def extract_education(text):
    """Extract the education section."""

    next_sections = [
        "SKILLS",
        "PROJECTS",
        "EXPERIENCE",
        "WORK EXPERIENCE",
        "INTERNSHIP",
        "CERTIFICATIONS"
    ]

    return extract_section(
        text,
        "EDUCATION",
        next_sections
    )


def extract_projects(text):
    """Extract the projects section."""

    next_sections = [
        "EXPERIENCE",
        "WORK EXPERIENCE",
        "INTERNSHIP",
        "CERTIFICATIONS",
        "EDUCATION",
        "SKILLS"
    ]

    return extract_section(
        text,
        "PROJECTS",
        next_sections
    )


def extract_experience(text):
    """Extract the experience section."""

    next_sections = [
        "PROJECTS",
        "EDUCATION",
        "SKILLS",
        "CERTIFICATIONS",
        "INTERNSHIP"
    ]

    return extract_section(
        text,
        "EXPERIENCE",
        next_sections
    )


def extract_resume_information(text):
    """
    Extract structured information from resume text.
    """

    cleaned_text = clean_text(text)

    resume_data = {
        "name": extract_name(cleaned_text),
        "email": extract_email(cleaned_text),
        "skills": extract_skills(cleaned_text),
        "education": extract_education(cleaned_text),
        "projects": extract_projects(cleaned_text),
        "experience": extract_experience(cleaned_text)
    }

    return resume_data