from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    ROLE_CHOICES = [('applicant', 'Applicant'), ('recruiter', 'Recruiter')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='applicant')

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",
        blank=True
    )