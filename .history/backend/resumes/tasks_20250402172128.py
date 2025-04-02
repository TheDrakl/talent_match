from celery import shared_task
import spacy
from PyPDF2 import PdfReader  # For extracting text from PDFs
from .models import Resume
import pytesseract
from PIL import Image

nlp = spacy.load("en_core_web_sm")

@shared_task
def process_resume(resume_id):
    resume = Resume.objects.get(id=resume_id)

    try:
        # Check file extension
        if resume.file.path.endswith(".pdf"):
            # Extract text from PDF
            reader = PdfReader(resume.file.path)
            text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
        elif resume.file.path.endswith(("jpg", "png", "jpeg")):
            img = Image.open(resume.file.path)
            text = pytesseract.image_to_string(img)
        else:
            raise ValueError("Unsupported file format")
        

        # Process text with SpaCy
        doc = nlp(text)
        skills = [ent.text for ent in doc.ents if ent.label_ in ["SKILL", "SKILLS", "LANGUAGE"]]
        experience = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "DATE"]]

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

