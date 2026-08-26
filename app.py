from pathlib import Path

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

from src.scorer import (
    calculate_education_score,
    calculate_experience_score,
    calculate_project_score,
    calculate_final_score
)

from src.ranker import rank_candidates

from src.ai_reasoning import (
    generate_candidate_reasoning
)

from src.exporter import (
    export_to_csv,
    export_to_json
)


def process_resume(
    resume_path,
    job_description_text,
    job_data
):
    """Process one resume and calculate all scores."""

    resume_text = extract_resume_text(
        resume_path
    )

    resume_data = extract_resume_information(
        resume_text
    )

    # -------------------------------------------------
    # NLP similarity
    # -------------------------------------------------

    similarity_score = calculate_text_similarity(
        resume_text,
        job_description_text
    )

    # -------------------------------------------------
    # Required skill matching
    # -------------------------------------------------

    skill_result = calculate_skill_match(
        resume_data["skills"],
        job_data["required_skills"]
    )

    skill_score = skill_result[
        "match_percentage"
    ]

    # -------------------------------------------------
    # Education
    # -------------------------------------------------

    education_score = calculate_education_score(
        resume_data["education"],
        job_data["education"]
    )

    # -------------------------------------------------
    # Experience
    # -------------------------------------------------

    experience_score = calculate_experience_score(
        resume_data["experience"],
        job_data["experience"]
    )

    # -------------------------------------------------
    # Projects
    # -------------------------------------------------

    project_score = calculate_project_score(
        resume_data["projects"],
        job_description_text
    )

    # -------------------------------------------------
    # Final score
    # -------------------------------------------------

    final_score = calculate_final_score(
        skill_score,
        similarity_score,
        education_score,
        experience_score,
        project_score
    )

    return {
        "name": resume_data["name"],
        "email": resume_data["email"],
        "resume_file": Path(resume_path).name,

        "final_score": final_score,

        "skill_score": skill_score,
        "nlp_score": similarity_score,
        "education_score": education_score,
        "experience_score": experience_score,
        "project_score": project_score,

        "matched_skills": ", ".join(
            skill_result["matched_skills"]
        ),

        "missing_skills": ", ".join(
            skill_result["missing_skills"]
        )
    }


def main():

    # -------------------------------------------------
    # File paths
    # -------------------------------------------------

    jd_path = "data/job_description.txt"

    resume_folder = Path(
        "data/sample_resumes"
    )

    output_folder = Path(
        "outputs"
    )

    try:

        # =================================================
        # 1. Load Job Description
        # =================================================

        jd_text = load_job_description(
            jd_path
        )

        job_data = extract_job_description(
            jd_text
        )

        print("\n" + "=" * 70)
        print("AI RESUME SCREENING AGENT")
        print("=" * 70)

        print(
            f"\nJob: {job_data['job_title']}"
        )

        # =================================================
        # 2. Find Resume Files
        # =================================================

        resume_files = []

        for extension in (
            "*.pdf",
            "*.docx",
            "*.txt"
        ):

            resume_files.extend(
                resume_folder.glob(extension)
            )

        if not resume_files:

            print("\nNo resume files found.")

            return

        print(
            f"\nFound {len(resume_files)} resume(s)."
        )

        # =================================================
        # 3. Process All Resumes
        # =================================================

        candidates = []

        for resume_path in resume_files:

            print(
                f"\nProcessing: "
                f"{resume_path.name}"
            )

            try:

                candidate = process_resume(
                    resume_path,
                    jd_text,
                    job_data
                )

                candidates.append(
                    candidate
                )

                print(
                    f"Score: "
                    f"{candidate['final_score']}/100"
                )

            except Exception as error:

                print(
                    f"Failed to process "
                    f"{resume_path.name}: "
                    f"{error}"
                )

        if not candidates:

            print(
                "\nNo candidates could be processed."
            )

            return

        # =================================================
        # 4. Rank Candidates
        # =================================================

        ranked_candidates = rank_candidates(
            candidates
        )

        # =================================================
        # 5. Generate Candidate Reasoning
        # =================================================

        print(
            "\nGenerating candidate reasoning..."
        )

        for candidate in ranked_candidates:

            print(
                f"Analyzing: "
                f"{candidate['name']}"
            )

            reasoning, reasoning_source = (
                generate_candidate_reasoning(
                    candidate,
                    jd_text
                )
            )

            candidate["reasoning"] = reasoning

            candidate["reasoning_source"] = (
                reasoning_source
            )

        # =================================================
        # 6. Export Results
        # =================================================

        csv_path = (
            output_folder
            / "ranked_candidates.csv"
        )

        json_path = (
            output_folder
            / "ranked_candidates.json"
        )

        export_to_csv(
            ranked_candidates,
            csv_path
        )

        export_to_json(
            ranked_candidates,
            json_path
        )

        # =================================================
        # 7. Display Final Ranking
        # =================================================

        print("\n" + "=" * 70)
        print("FINAL RANKED CANDIDATES")
        print("=" * 70)

        for candidate in ranked_candidates:

            print(
                f"\n#{candidate['rank']} "
                f"{candidate['name']}"
            )

            print(
                f"Score: "
                f"{candidate['final_score']}/100"
            )

            print(
                f"Matched Skills: "
                f"{candidate['matched_skills']}"
            )

            print(
                f"Missing Skills: "
                f"{candidate['missing_skills']}"
            )

            print(
                f"Reasoning Source: "
                f"{candidate['reasoning_source']}"
            )

            print(
                "\nRECRUITMENT ASSESSMENT:"
            )

            print(
                candidate["reasoning"]
            )

            print("-" * 70)

        # =================================================
        # 8. Final Summary
        # =================================================

        print(
            f"\nProcessed "
            f"{len(ranked_candidates)} "
            f"candidate(s)."
        )

        print(
            "\nResults exported successfully:"
        )

        print(
            f"CSV : {csv_path}"
        )

        print(
            f"JSON: {json_path}"
        )

        print(
            "\nSCREENING COMPLETED SUCCESSFULLY"
        )

    except Exception as error:

        print(
            f"\nError: {error}"
        )


if __name__ == "__main__":
    main()