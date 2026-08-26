# AI Resume Screening Agent

An AI-assisted Resume Screening Agent that parses resumes, extracts candidate information, compares candidates against a Job Description, calculates relevance scores, ranks candidates, and generates recruitment reasoning.

## Features

- Resume parsing for TXT, PDF, and DOCX files
- Resume information extraction
- Job Description parsing
- Required skill matching
- TF-IDF and cosine similarity
- Education matching
- Experience matching
- Project relevance scoring
- Weighted candidate scoring
- Batch processing of 10+ resumes
- Candidate ranking
- AI reasoning with rule-based fallback
- CSV output
- JSON output
- Automated tests

## Project Structure

```text
AI-Resume-Screening-Agent/
│
├── data/
│   ├── job_description.txt
│   └── sample_resumes/
│
├── src/
│   ├── resume_parser.py
│   ├── extractor.py
│   ├── jd_parser.py
│   ├── matcher.py
│   ├── scorer.py
│   ├── ranker.py
│   ├── ai_reasoning.py
│   └── exporter.py
│
├── outputs/
│   ├── ranked_candidates.csv
│   └── ranked_candidates.json
│
├── tests/
│   └── test_screening.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore