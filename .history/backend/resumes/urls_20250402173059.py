from django.urls import path
from .views import ResumeListCreateAPIView

urlpatterns = [
    path('publish/', ResumeListCreateAPIView, name='publish_resume'),
]