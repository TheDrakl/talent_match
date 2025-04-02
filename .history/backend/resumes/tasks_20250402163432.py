from celery import shared_task
import spacy
from .models import Resume

n1p = spacy.load()