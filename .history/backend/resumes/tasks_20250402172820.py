from celery import shared_task
import spacy
from PyPDF2 import PdfReader
from .models import Resume
import pytesseract
from PIL import Image
import re

nlp = spacy.load("en_core_web_sm")

SKILLS_KEYWORDS = [
    "Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "Django", "Flask",
    "React", "Angular", "AWS", "Docker", "Kubernetes", "Git", "Machine Learning",
    "Deep Learning", "Data Analysis", "Project Management", "Agile", "Scrum", "Time Managment", "Problem-Solving", "MultiTasking"
]

@shared_task
def process_resume(resume_id):
    resume = Resume.objects.get(id=resume_id)

    try:
        if resume.file.path.endswith(".pdf"):
            reader = PdfReader(resume.file.path)
            text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
        elif resume.file.path.endswith(("jpg", "png", "jpeg")):
            img = Image.open(resume.file.path)
            text = pytesseract.image_to_string(img)
        else:
            raise ValueError("Unsupported file format")
        
        doc = nlp(text)


        skills = [skill for skill in SKILLS_KEYWORDS if skill.lower() in text.lower()]

        # Extract experience using NER and regex
        experience = []
        for ent in doc.ents:
            if ent.label_ in ["ORG"]:
                experience.append(ent.text)
            elif ent.label_ == "DATE":
                experience.append(ent.text)
        job_title_pattern = r"\b(?:Software Engineer|Data Scientist|Project Manager|Developer|Analyst|Consultant)\b"
        job_titles = re.findall(job_title_pattern, text, re.IGNORECASE)
        experience.extend(job_titles)

        # Remove duplicates and clean up
        skills = list(set(skills))
        experience = list(set(experience))

        # Update the Resume object
        resume.skills = skills
        resume.experience = experience
        resume.processed = True
        resume.save()

    except Exception as e:
        # Handle errors (e.g., unsupported file formats or extraction issues)
        resume.processed = False
        resume.save()
        raise e