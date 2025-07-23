import pdfplumber
import re
import spacy

# Load English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a given PDF file.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_name(text):
    """
    Try to extract the name from the first non-empty line 
    that doesn't contain email or phone patterns.
    If not found, fallback to spaCy NER.
    """
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line and not re.search(r'@|\d', line):
            return line

    # Fallback to spaCy NER
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return None


def extract_email(text):
    """
    Extract the first email address found in the text.
    """
    match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    return match.group(0) if match else None


def extract_phone(text):
    """
    Extract the first phone number found in the text.
    """
    match = re.search(r"\+?\d[\d\-\(\) ]{7,}\d", text)
    return match.group(0) if match else None


def extract_skills(text, skills_db):
    """
    Return a list of known skills found in the resume text.
    """
    found_skills = []
    text_lower = text.lower()
    for skill in skills_db:
        if skill.lower() in text_lower:
            found_skills.append(skill)
    return list(set(found_skills))  # Remove duplicates


def parse_resume(pdf_path, skills_db):
    """
    Main function to parse a resume PDF and return extracted info.
    """
    text = extract_text_from_pdf(pdf_path)

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text, skills_db)
    }
