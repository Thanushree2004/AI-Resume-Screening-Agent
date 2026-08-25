from src.resume_parser import extract_resume_text
from src.extractor import extract_resume_information


def main():
    resume_path = "data/sample_resumes/sample_resume.txt"

    try:
        resume_text = extract_resume_text(resume_path)

        resume_data = extract_resume_information(resume_text)

        print("\n" + "=" * 60)
        print("AI RESUME SCREENING AGENT")
        print("=" * 60)

        print("\nNAME:")
        print(resume_data["name"])

        print("\nEMAIL:")
        print(resume_data["email"])

        print("\nSKILLS:")
        print(resume_data["skills"])

        print("\nEDUCATION:")
        print(resume_data["education"])

        print("\nPROJECTS:")
        print(resume_data["projects"])

        print("\nEXPERIENCE:")
        print(resume_data["experience"])

        print("\n" + "=" * 60)
        print("RESUME INFORMATION EXTRACTION SUCCESSFUL")
        print("=" * 60)

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()