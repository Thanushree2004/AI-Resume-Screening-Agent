````markdown
# AI Resume Screening Agent

An AI-assisted Resume Screening Agent that automates candidate evaluation against a Job Description (JD). The system parses resumes, extracts candidate information, performs skill and NLP-based matching, calculates a weighted suitability score, ranks candidates, and generates recruitment assessments.

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Thanushree2004/AI-Resume-Screening-Agent.git
cd AI-Resume-Screening-Agent
````

### 2. Create a Virtual Environment

Windows PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run the Application

```powershell
python app.py
```

The application automatically processes the Job Description and all supported resumes in `data/sample_resumes/`.

### 5. View the Results

After execution, the ranked results are generated in:

```text
outputs/
├── ranked_candidates.csv
└── ranked_candidates.json
```

### 6. Run Tests

```powershell
python -m pytest
```

Expected result:

```text
7 passed
```

> **Note:** An OpenAI API key is optional for the core screening pipeline. If LLM access is unavailable or the API quota is exhausted, the application automatically uses its rule-based reasoning fallback.

---

## Features

* Resume parsing for TXT, PDF, and DOCX files
* Candidate information extraction
* Job Description parsing
* Required skill matching
* TF-IDF and cosine similarity-based NLP matching
* Education compatibility analysis
* Experience compatibility analysis
* Project relevance analysis
* Weighted candidate scoring
* Batch screening of 10+ resumes
* Candidate ranking
* AI-assisted recruitment reasoning
* Rule-based reasoning fallback
* CSV output generation
* JSON output generation
* Automated testing with pytest

---

## Technology Stack

| Category             | Technology                |
| -------------------- | ------------------------- |
| Programming Language | Python                    |
| NLP                  | TF-IDF, Cosine Similarity |
| Document Processing  | TXT, PDF, DOCX            |
| AI                   | OpenAI API                |
| Testing              | Pytest                    |
| Data Output          | CSV, JSON                 |
| Version Control      | Git, GitHub               |

---

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
```

---

## Requirements

* Python 3.10 or higher
* pip
* Git
* Optional OpenAI API access for LLM-based reasoning

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Thanushree2004/AI-Resume-Screening-Agent.git
```

Navigate to the project:

```bash
cd AI-Resume-Screening-Agent
```

Create a virtual environment:

```powershell
python -m venv venv
```

Activate the environment:

```powershell
venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

---

## Configuration

The project supports optional OpenAI API-based recruitment reasoning.

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

The API key should never be committed to GitHub.

The `.env` file is excluded using `.gitignore`.

### API Availability

The application does not depend entirely on the OpenAI API.

If the API is unavailable, incorrectly configured, or the API quota is exhausted, the system automatically uses a rule-based reasoning fallback.

This allows the core screening, scoring, ranking, and export pipeline to continue functioning.

---

## Input Data

### Job Description

The Job Description is stored at:

```text
data/job_description.txt
```

### Candidate Resumes

Candidate resumes are stored in:

```text
data/sample_resumes/
```

Supported formats:

* TXT
* PDF
* DOCX

The project includes 10+ sample resumes for batch screening and ranking.

---

## How the Application Works

The application follows an end-to-end screening pipeline:

```text
Job Description
       │
       ▼
   JD Parsing
       │
       ▼
Required Skills
       │
       │
       ▼
 Resume Files
       │
       ▼
Resume Parsing
       │
       ▼
Information Extraction
       │
       ├── Skills
       ├── Education
       ├── Experience
       └── Projects
       │
       ▼
Candidate Matching
       │
       ├── Skill Matching
       ├── NLP Similarity
       ├── Education
       ├── Experience
       └── Project Relevance
       │
       ▼
Weighted Candidate Score
       │
       ▼
Candidate Ranking
       │
       ▼
Recruitment Reasoning
       │
       ▼
 CSV + JSON Results
```

---

## Scoring Methodology

The final candidate score is calculated using the following weighted components:

| Evaluation Component |   Weight |
| -------------------- | -------: |
| Required Skill Match |      50% |
| NLP Similarity       |      20% |
| Education Match      |      15% |
| Experience Match     |      10% |
| Project Relevance    |       5% |
| **Total**            | **100%** |

### Required Skill Match

The candidate's extracted skills are compared with the required skills from the Job Description.

The system identifies:

* Matched skills
* Missing skills
* Skill match percentage

### NLP Similarity

TF-IDF vectorization and cosine similarity are used to measure textual similarity between the resume and the Job Description.

### Education Match

The candidate's educational background is evaluated against the educational requirements specified in the Job Description.

### Experience Match

Candidate experience is compared with the requirements of the role.

Fresher candidates are supported when the Job Description permits entry-level applicants.

### Project Relevance

Candidate projects are evaluated using technical keywords relevant to the target role.

### Final Score

The individual scores are combined according to the defined weights to produce a final suitability score between 0 and 100.

---

## Candidate Ranking

Candidates are ranked in descending order based on their final suitability score.

The highest-scoring candidate receives Rank 1.

Example:

```text
Rank 1 → ARJUN SHARMA → 79.15
Rank 2 → SNEHA KUMAR  → 78.41
Rank 3 → PRIYA REDDY  → 73.26
```

---

## AI Recruitment Reasoning

The system supports two reasoning modes.

### LLM-Based Reasoning

When OpenAI API access is available, the system can generate a recruitment assessment based on:

* Candidate score
* Matched skills
* Missing skills
* Education
* Experience
* Project relevance
* Job Description requirements

The assessment provides:

* Overall assessment
* Key strengths
* Missing or weak areas
* Score explanation
* Recommendation

### Rule-Based Fallback

If the OpenAI API is unavailable or the API quota is exhausted, the application automatically generates a rule-based recruitment assessment.

The fallback uses:

* Final score
* Skill match
* NLP similarity
* Education match
* Experience match
* Project relevance
* Matched skills
* Missing skills

The reasoning source is displayed as:

```text
llm
```

or:

```text
rule-based-fallback
```

---

## Output

The application generates two ranked result files.

### CSV

```text
outputs/ranked_candidates.csv
```

### JSON

```text
outputs/ranked_candidates.json
```

Each candidate record contains:

* Rank
* Candidate name
* Email
* Resume filename
* Final score
* Skill score
* NLP similarity score
* Education score
* Experience score
* Project score
* Matched skills
* Missing skills
* Reasoning source
* Recruitment assessment

---

## Example Output

```text
======================================================================
FINAL RANKED CANDIDATES
======================================================================

#1 ARJUN SHARMA
Score: 79.15/100

Matched Skills:
css, django, flask, git, html, javascript, python, rest api, sql

Missing Skills:
None

Reasoning Source:
rule-based-fallback

RECRUITMENT ASSESSMENT:

The candidate is a strong match for the
Junior Python Developer role.
```

---

## Automated Testing

The project includes an automated test suite using `pytest`.

Run:

```powershell
python -m pytest
```

Current test result:

```text
7 passed
```

The test suite covers:

* NLP similarity
* Skill matching
* Education scoring
* Experience scoring
* Project relevance
* Final score validation
* Candidate ranking

---

## Design Decisions and Trade-offs

### TF-IDF Instead of Embeddings

TF-IDF was selected because it is lightweight, fast, interpretable, and easy to reproduce.

Embedding-based semantic matching could provide stronger contextual understanding but would introduce additional model dependencies and complexity.

### Weighted Scoring

Required technical skills receive the highest weight because technical skill alignment is a primary factor in resume screening.

### Rule-Based Fallback

LLM-based reasoning depends on external API availability and quota.

The fallback ensures that the core screening and ranking workflow remains operational when the external AI service is unavailable.

---

## Limitations

* Resume formatting can affect extraction accuracy.
* Skill extraction relies on predefined matching logic.
* TF-IDF similarity does not provide complete semantic understanding.
* Project relevance is estimated using technical keyword matching.
* The system is intended as a recruitment screening aid and should not replace human decision-making.
* Sample resumes are intended for demonstration and testing.

---

## Security Considerations

* API credentials are stored in `.env`.
* `.env` is excluded through `.gitignore`.
* API keys must never be committed to GitHub.
* Confidential candidate information should not be uploaded to a public repository.

---

## Testing Status

| Component                     | Status     |
| ----------------------------- | ---------- |
| Resume Parsing                | Complete   |
| Resume Information Extraction | Complete   |
| Job Description Parsing       | Complete   |
| Skill Matching                | Complete   |
| NLP Matching                  | Complete   |
| Education Matching            | Complete   |
| Experience Matching           | Complete   |
| Project Relevance             | Complete   |
| Weighted Scoring              | Complete   |
| Batch Processing              | Complete   |
| Candidate Ranking             | Complete   |
| AI Reasoning                  | Complete   |
| Rule-Based Fallback           | Complete   |
| CSV Export                    | Complete   |
| JSON Export                   | Complete   |
| Automated Testing             | 7/7 Passed |
| Documentation                 | Complete   |

---

## Project Status

The project is implemented as an end-to-end resume screening pipeline capable of processing multiple candidates, ranking them against a target Job Description, generating recruitment assessments, and exporting structured results.

---

## License

This project is intended for educational and demonstration purposes.

````

### After replacing the README

Save it with **Ctrl + S**, then run:

```powershell
git add README.md
git commit -m "Improve README documentation"
git push origin main
````