from parser import parse_resume
from recommender import load_job_data, recommend_jobs
import json

# Sample list of known skills (can be expanded)
skills_database = [
    "Python", "Java", "C++", "HTML", "CSS", "JavaScript",
    "SQL", "NoSQL", "Django", "Flask", "Git", "Docker",
    "Machine Learning", "Deep Learning", "Data Analysis", "Pandas"
]

# Sample resume file (should exist in the same folder)
resume_file = "sample_resume.pdf"

# Parse the resume
parsed_data = parse_resume(resume_file, skills_database)

# Save parsed data to JSON file
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(parsed_data, f, indent=2)

# Display parsed results
print("🔍 Resume Analysis Result:")
for key, value in parsed_data.items():
    print(f"{key.capitalize()}: {value}")

# Load job titles and skills dataset
job_data = load_job_data("job_titles.json")

# Recommend job titles based on parsed skills
recommended = recommend_jobs(parsed_data["skills"], job_data)

# Show recommendations
print("\n💼 Recommended Job Titles:")
for title, score in recommended:
    print(f"{title} ({score}% match)")
