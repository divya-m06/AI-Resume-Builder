from app.services.nlp_service import extract_skills


def analyze_skill_gap(job_role, resume_text, additional_skills=None):
    """
    Analyze skill gap between job role requirements and resume content.
    Returns found skills, missing skills, resume score, suggestions, and interview questions.
    """

    # Job skills mapping
    job_skills = {
        "java developer": [
            "java", "sql", "cloud computing"
        ],
        "python developer": [
            "python", "sql", "machine learning", "ai"
        ],
        "data analyst": [
            "python", "sql", "big data", "statistics"
        ],
        "project manager": [
            "cloud computing", "networking"
        ],
        "data scientist": [
            "python", "machine learning", "deep learning", "ai", "big data"
        ],
        "aiml engineer": [
            "python", "machine learning", "deep learning", "ai"
        ],
        "software developer": [
            "java", "python", "sql"
        ],
        "full stack developer": [
            "react", "nodejs", "sql", "cloud computing"
        ],
        "frontend developer": [
            "react", "javascript"
        ],
        "backend developer": [
            "java", "python", "sql", "nodejs"
        ],
        "cloud engineer": [
            "cloud computing", "kubernetes", "networking"
        ],
        "devops engineer": [
            "cloud computing", "kubernetes", "networking"
        ],
        "cybersecurity analyst": [
            "cybersecurity", "networking", "cloud computing"
        ],
        "big data engineer": [
            "big data", "python", "sql", "cloud computing"
        ],
        "network engineer": [
            "networking", "cybersecurity"
        ],
        "ai engineer": [
            "ai", "machine learning", "deep learning", "python"
        ]
    }

    expected = job_skills.get(job_role.lower(), [])

    # Add additional skills if provided
    if additional_skills:
        additional_list = [s.strip().lower() for s in additional_skills.split(",") if s.strip()]
        expected.extend(additional_list)

    resume_skills_set = {s.lower() for s in extract_skills(resume_text)}

    found_skills = [s for s in expected if s.lower() in resume_skills_set]
    missing_skills = [s for s in expected if s not in found_skills]

    # Calculate score
    resume_score = int((len(found_skills) / len(expected)) * 100) if expected else 0

    # Course suggestions
    suggestions = []
    for skill in missing_skills:
        suggestions.append({
            "skill": skill.title(),
            "courses": [
                {"title": f"{skill.title()} – Coursera", "link": f"https://www.coursera.org/search?query={skill}"},
                {"title": f"{skill.title()} – Udemy", "link": f"https://www.udemy.com/courses/search/?q={skill}"},
                {"title": f"{skill.title()} – YouTube", "link": f"https://www.youtube.com/results?search_query={skill}"}
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
        "interview_questions": []   # Populated by Groq in the API route (main.py)
    }
