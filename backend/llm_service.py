import os
import json
from groq import Groq

def generate_learning_roadmap(job_role, missing_skills, experience_level="beginner"):
    """
    Generate a week-by-week learning roadmap for missing skills using Groq API.
    Returns a list of {week, focus_skill, why_it_matters, action_items}.
    """

    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        prompt = f"""
        Create a 4-week learning roadmap for someone wanting to become a {job_role}.
        They are missing these skills: {', '.join(missing_skills)}
        Experience level: {experience_level}

        Return ONLY valid JSON in this exact format:
        [
            {{
                "week": 1,
                "focus_skill": "Skill Name",
                "why_it_matters": "Brief explanation of importance",
                "action_items": ["Action 1", "Action 2", "Action 3"]
            }},
            {{
                "week": 2,
                "focus_skill": "Skill Name",
                "why_it_matters": "Brief explanation of importance",
                "action_items": ["Action 1", "Action 2", "Action 3"]
            }}
        ]

        Focus on practical, actionable steps. Distribute the missing skills across the 4 weeks.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )

        content = response.choices[0].message.content.strip()

        # Remove markdown fences if present
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]

        content = content.strip()

        # Parse JSON
        roadmap = json.loads(content)

        # Validate structure
        if not isinstance(roadmap, list):
            raise ValueError("Response is not a list")

        for item in roadmap:
            required_keys = ["week", "focus_skill", "why_it_matters", "action_items"]
            if not all(key in item for key in required_keys):
                raise ValueError(f"Missing required keys in item: {item}")

        return roadmap

    except Exception as e:
        print(f"Error generating roadmap: {e}")
        # Fallback roadmap
        return [
            {
                "week": 1,
                "focus_skill": missing_skills[0] if missing_skills else "General Skills",
                "why_it_matters": "Essential for the role",
                "action_items": [
                    "Research the skill online",
                    "Find learning resources",
                    "Start with basics"
                ]
            },
            {
                "week": 2,
                "focus_skill": missing_skills[1] if len(missing_skills) > 1 else "Practice",
                "why_it_matters": "Builds practical experience",
                "action_items": [
                    "Work on small projects",
                    "Practice regularly",
                    "Get feedback"
                ]
            }
        ]