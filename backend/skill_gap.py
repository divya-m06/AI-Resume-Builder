import spacy
from rapidfuzz import fuzz, process
from spacy.matcher import PhraseMatcher

# Load spaCy model — must be downloaded first with:
# python -m spacy download en_core_web_sm
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    nlp = None
    print("Warning: spaCy model not loaded. Run: python -m spacy download en_core_web_sm")

# Expanded job skills mapping
job_skills = {
    "java developer": [
        "Java", "Spring Boot", "Maven", "Hibernate", "SQL", "REST API",
        "Microservices", "JUnit", "Git", "Cloud Computing"
    ],
    "python developer": [
        "Python", "Django", "Flask", "FastAPI", "SQL", "Machine Learning",
        "REST API", "Git", "Docker", "NumPy", "Pandas"
    ],
    "data analyst": [
        "Python", "SQL", "Excel", "Tableau", "Power BI", "Statistics",
        "Data Visualization", "Pandas", "NumPy", "Big Data"
    ],
    "project manager": [
        "Agile", "Scrum", "JIRA", "Risk Management", "Stakeholder Management",
        "Budgeting", "MS Project", "Communication", "Leadership"
    ],
    "data scientist": [
        "Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
        "SQL", "Statistics", "NLP", "Big Data", "Scikit-learn", "Pandas"
    ],
    "aiml engineer": [
        "Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
        "NLP", "Computer Vision", "Scikit-learn", "Docker", "MLOps"
    ],
    "software developer": [
        "Java", "Python", "SQL", "Git", "REST API", "OOP",
        "Data Structures", "Algorithms", "Agile", "Testing"
    ],
    "full stack developer": [
        "React", "Node.js", "JavaScript", "SQL", "MongoDB", "REST API",
        "Git", "Docker", "CSS", "HTML", "TypeScript"
    ],
    "frontend developer": [
        "React", "JavaScript", "TypeScript", "HTML", "CSS", "Tailwind CSS",
        "Redux", "Git", "Responsive Design", "REST API"
    ],
    "backend developer": [
        "Java", "Python", "Node.js", "SQL", "MongoDB", "REST API",
        "Docker", "Git", "Microservices", "Authentication"
    ],
    "cloud engineer": [
        "AWS", "Azure", "GCP", "Kubernetes", "Docker", "Terraform",
        "Networking", "Linux", "CI/CD", "Cloud Security"
    ],
    "devops engineer": [
        "Docker", "Kubernetes", "Jenkins", "CI/CD", "AWS", "Terraform",
        "Linux", "Git", "Monitoring", "Ansible"
    ],
    "cybersecurity analyst": [
        "Network Security", "SIEM", "Penetration Testing", "Firewalls",
        "Cryptography", "Incident Response", "Linux", "Python", "Compliance"
    ],
    "big data engineer": [
        "Apache Spark", "Hadoop", "Kafka", "SQL", "Python", "Scala",
        "Cloud Computing", "ETL", "Hive", "Data Warehousing"
    ],
    "network engineer": [
        "TCP/IP", "Routing", "Switching", "Firewalls", "VPN",
        "Network Security", "Cisco", "Linux", "DNS", "DHCP"
    ],
    "ai engineer": [
        "Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
        "NLP", "Computer Vision", "MLOps", "Docker", "REST API"
    ]
}


def extract_skills_from_resume(resume_text, skill_list):
    """
    Use spaCy PhraseMatcher + rapidfuzz to find skills in resume text.
    Returns list of matched skills from skill_list.
    """
    if not skill_list:
        return []

    if not nlp:
        # Fallback to basic string matching if spaCy not available
        resume_lower = resume_text.lower()
        return [s for s in skill_list if s.lower() in resume_lower]

    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(skill.lower()) for skill in skill_list]
    matcher.add("SKILLS", patterns)

    doc = nlp(resume_text[:100000])  # limit to 100k chars for performance
    spacy_matches = set()
    for match_id, start, end in matcher(doc):
        spacy_matches.add(doc[start:end].text.lower())

    resume_lower = resume_text.lower()

    # Fuzzy matching for typos / spacing variations (threshold 85)
    fuzzy_matches = set()
    step = max(len(resume_lower) // 200, 1)
    windows = [
        resume_lower[i : i + min(120, len(resume_lower) - i)]
        for i in range(0, min(len(resume_lower), 50000), step)
    ]
    if not windows:
        windows = [resume_lower]

    for skill in skill_list:
        q = skill.lower()
        result = process.extractOne(
            q,
            windows,
            scorer=fuzz.partial_ratio,
            score_cutoff=85,
        )
        if result:
            fuzzy_matches.add(q)
            continue
        if fuzz.partial_ratio(q, resume_lower) >= 85:
            fuzzy_matches.add(q)

    all_matched_lower = spacy_matches | fuzzy_matches
    found = [s for s in skill_list if s.lower() in all_matched_lower]
    return found


def analyze_skill_gap(job_role, resume_text, additional_skills=None):
    """
    Analyze skill gap using spaCy NLP + rapidfuzz fuzzy matching.
    """
    expected = list(job_skills.get(job_role.lower(), []))

    if additional_skills:
        additional_list = [s.strip() for s in additional_skills.split(",") if s.strip()]
        expected.extend(additional_list)

    if not expected:
        return {
            "job_role": job_role,
            "resume_score": 0,
            "ats_result": {"found": [], "missing": []},
            "suggestions": [],
            "interview_questions": []
        }

    found_skills = extract_skills_from_resume(resume_text, expected)
    found_lower = {s.lower() for s in found_skills}
    missing_skills = [s for s in expected if s.lower() not in found_lower]

    resume_score = int((len(found_skills) / len(expected)) * 100) if expected else 0

    suggestions = []
    for skill in missing_skills:
        suggestions.append({
            "skill": skill,
            "courses": [
                {"title": f"{skill} – Coursera", "link": f"https://www.coursera.org/search?query={skill.replace(' ', '+')}"},
                {"title": f"{skill} – Udemy", "link": f"https://www.udemy.com/courses/search/?q={skill.replace(' ', '+')}"},
                {"title": f"{skill} – YouTube", "link": f"https://www.youtube.com/results?search_query={skill.replace(' ', '+')}"}
            ]
        })

    return {
        "job_role": job_role,
        "resume_score": resume_score,
        "ats_result": {
            "found": found_skills,
            "missing": missing_skills
        },
        "suggestions": suggestions,
        "interview_questions": []  # Populated by Groq in main.py
    }
