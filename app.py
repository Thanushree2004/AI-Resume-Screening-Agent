from src.resume_parser import extract_resume_text
from src.extractor import extract_resume_information

from src.jd_parser import (
    load_job_description,
    extract_job_description
)

from src.matcher import (
    calculate_text_similarity,
    calculate_skill_match
)


def main():

    resume_path = "data/sample_resumes/sample_resume.txt"
    jd_path = "data/job_description.txt"

    try:

        # -------------------------------------------------
        # 1. Read Resume
        # -------------------------------------------------

        resume_text = extract_resume_text(
            resume_path
        )

        resume_data = extract_resume_information(
            resume_text
        )

        # -------------------------------------------------
        # 2. Read Job Description
        # -------------------------------------------------

        jd_text = load_job_description(
            jd_path
        )

        job_data = extract_job_description(
            jd_text
        )

        # -------------------------------------------------
        # 3. Calculate NLP Similarity
        # -------------------------------------------------

        similarity_score = calculate_text_similarity(
            resume_text,
            jd_text
        )

        # -------------------------------------------------
        # 4. Calculate Skill Match
        # -------------------------------------------------

        skill_result = calculate_skill_match(
            resume_data["skills"],
            job_data["required_skills"]
        )

        # -------------------------------------------------
        # 5. Display Results
        # -------------------------------------------------

        print("\n" + "=" * 60)
        print("AI RESUME SCREENING - NLP MATCHING")
        print("=" * 60)

        print("\nCANDIDATE:")
        print(resume_data["name"])

        print("\nJOB:")
        print(job_data["job_title"])

        print("\nNLP SIMILARITY SCORE:")
        print(f"{similarity_score}%")

        print("\nMATCHED SKILLS:")

        if skill_result["matched_skills"]:
            for skill in skill_result["matched_skills"]:
                print(f"  ✓ {skill}")

        else:
            print("  None")

        print("\nMISSING SKILLS:")

        if skill_result["missing_skills"]:
            for skill in skill_result["missing_skills"]:
                print(f"  ✗ {skill}")

        else:
            print("  None")

        print("\nSKILL MATCH SCORE:")
        print(
            f"{skill_result['match_percentage']}%"
        )

        print("\n" + "=" * 60)
        print("NLP MATCHING SUCCESSFUL")
        print("=" * 60)

    except Exception as error:

        print(f"\nError: {error}")


if __name__ == "__main__":
    main()