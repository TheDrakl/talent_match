from celery import shared_task
import spacy
from .models import Resume

n1p = spacy.load("en_core_web_sm")

@shared_task
def process_resume(resume_id):
    resume = Resume.objects.get(id=resume_id)

    with open(resume.file.path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    doc = nlp(text)
