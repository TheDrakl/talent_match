from django.db import models
from django.contrib.auth import get_user_model
from ..users.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    extracted_text = models.CharField(blank=True)
    skills = models.JSONField(default=list)
    experience = models.JSONField(default=list)
    processed = models.BooleanField(default=False)