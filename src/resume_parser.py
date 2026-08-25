from pathlib import Path
from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(file_path):
    """Extract text from a PDF resume."""
    reader = PdfReader(file_path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages).strip()


def extract_text_from_docx(file_path):
    """Extract text from a DOCX resume."""
    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs).strip()


def extract_text_from_txt(file_path):
    """Extract text from a TXT resume."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()


def extract_resume_text(file_path):
    """
    Detect the file type and extract resume text.

    Supported formats:
    PDF, DOCX, TXT
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(path)

    elif extension == ".docx":
        return extract_text_from_docx(path)

    elif extension == ".txt":
        return extract_text_from_txt(path)

    else:
        raise ValueError(
            f"Unsupported file format: {extension}. "
            "Use PDF, DOCX, or TXT."
        )


if __name__ == "__main__":
    print("Resume Parser Module")
    print("Supported formats: PDF, DOCX, TXT")