import csv
import json
from pathlib import Path


FIELDS = [
    "rank",
    "name",
    "email",
    "resume_file",
    "final_score",
    "skill_score",
    "nlp_score",
    "education_score",
    "experience_score",
    "project_score",
    "matched_skills",
    "missing_skills",
    "reasoning_source",
    "reasoning"
]


def export_to_csv(candidates, output_path):
    """Export ranked candidates to CSV."""

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELDS
        )

        writer.writeheader()

        for candidate in candidates:

            writer.writerow({
                field: candidate.get(
                    field,
                    ""
                )
                for field in FIELDS
            })


def export_to_json(candidates, output_path):
    """Export ranked candidates to JSON."""

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            candidates,
            file,
            indent=4,
            ensure_ascii=False
        )