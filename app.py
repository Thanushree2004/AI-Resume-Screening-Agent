from src.jd_parser import (
    load_job_description,
    extract_job_description
)


def main():

    jd_path = "data/job_description.txt"

    try:
        # Load the Job Description
        jd_text = load_job_description(jd_path)

        # Extract structured information
        job_data = extract_job_description(jd_text)

        print("\n" + "=" * 60)
        print("JOB DESCRIPTION ANALYZER")
        print("=" * 60)

        print("\nJOB TITLE:")
        print(job_data["job_title"])

        print("\nEDUCATION:")
        print(job_data["education"])

        print("\nREQUIRED SKILLS:")
        print(job_data["required_skills"])

        print("\nPREFERRED SKILLS:")
        print(job_data["preferred_skills"])

        print("\nEXPERIENCE:")
        print(job_data["experience"])

        print("\nRESPONSIBILITIES:")
        print(job_data["responsibilities"])

        print("\n" + "=" * 60)
        print("JOB DESCRIPTION PARSING SUCCESSFUL")
        print("=" * 60)

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()