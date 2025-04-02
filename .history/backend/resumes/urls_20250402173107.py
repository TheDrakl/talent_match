from django.urls import path
from .views import ResumeListCreateAPIView

urlpatterns = [
    path('publish/', ResumeListCreateAPIView.as_view, name='publish_resume'),
]