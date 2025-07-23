import json
from fuzzywuzzy import fuzz  # در حال حاضر استفاده نشده، اما می‌تونی برای مقایسه دقیق‌تر استفاده کنی

def load_job_data(json_path):
    """
    Load job titles and related skills from a JSON file.
    Args:
        json_path (str): Path to the JSON file.
    Returns:
        dict: Dictionary with job titles as keys and list of required skills as values.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def recommend_jobs(user_skills, job_data, top_n=3):
    """
    Recommend job titles based on skill matching.
    Args:
        user_skills (list): List of skills extracted from the resume.
        job_data (dict): Job titles and their required skills.
        top_n (int): Number of top recommendations to return.
    Returns:
        list of tuples: [(job_title, match_percentage), ...] sorted by match_percentage descending.
    """
    recommendations = []

    user_skills_lower = set(skill.lower() for skill in user_skills)

    for job_title, required_skills in job_data.items():
        required_skills_lower = set(skill.lower() for skill in required_skills)
        match_count = len(user_skills_lower & required_skills_lower)
        total_skills = len(required_skills_lower)
        match_percent = int((match_count / total_skills) * 100) if total_skills > 0 else 0
        
        recommendations.append((job_title, match_percent))

    # Sort by highest match percentage
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations[:top_n]
