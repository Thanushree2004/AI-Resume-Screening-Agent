import re


def clean_text(text):
    """Clean unnecessary spaces and blank lines."""

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n+", "\n", text)

    return text.strip()


def extract_section(text, section_name, next_sections):
    """Extract a specific section from the job description."""

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


def extract_job_title(text):
    """Extract the first line as the job title."""

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if lines:
        return lines[0]

    return "Not Found"


def extract_education(text):
    """Extract education requirements."""

    sections = [
        "REQUIRED SKILLS",
        "PREFERRED SKILLS",
        "EXPERIENCE",
        "RESPONSIBILITIES"
    ]

    return extract_section(
        text,
        "EDUCATION",
        sections
    )


def extract_required_skills(text):
    """Extract required skills."""

    sections = [
        "PREFERRED SKILLS",
        "EXPERIENCE",
        "RESPONSIBILITIES"
    ]

    return extract_section(
        text,
        "REQUIRED SKILLS",
        sections
    )


def extract_preferred_skills(text):
    """Extract preferred skills."""

    sections = [
        "EXPERIENCE",
        "RESPONSIBILITIES"
    ]

    return extract_section(
        text,
        "PREFERRED SKILLS",
        sections
    )


def extract_experience(text):
    """Extract experience requirements."""

    sections = [
        "RESPONSIBILITIES"
    ]

    return extract_section(
        text,
        "EXPERIENCE",
        sections
    )


def extract_responsibilities(text):
    """Extract job responsibilities."""

    sections = []

    return extract_section(
        text,
        "RESPONSIBILITIES",
        sections
    )


def extract_job_description(text):
    """Extract structured information from the job description."""

    cleaned_text = clean_text(text)

    job_data = {
        "job_title": extract_job_title(cleaned_text),
        "education": extract_education(cleaned_text),
        "required_skills": extract_required_skills(cleaned_text),
        "preferred_skills": extract_preferred_skills(cleaned_text),
        "experience": extract_experience(cleaned_text),
        "responsibilities": extract_responsibilities(cleaned_text)
    }

    return job_data


def load_job_description(file_path):
    """Load the job description from a text file."""

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()