def rank_candidates(candidates):
    """
    Sort candidates from highest score to lowest score.
    """

    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: candidate["final_score"],
        reverse=True
    )

    for index, candidate in enumerate(
        ranked_candidates,
        start=1
    ):
        candidate["rank"] = index

    return ranked_candidates