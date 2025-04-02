from django.urls import path
from .views import ResumeListCreateAPIView

urlpatterns = [
    path('publish/', resume_list, name='publish_resume'),
]