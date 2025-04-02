from rest_framework.viewsets import generics
from rest_framework.permissions import IsAuthenticated
from .models import Resume
from .tasks import process_resume
from .serializers import ResumeSerializer
