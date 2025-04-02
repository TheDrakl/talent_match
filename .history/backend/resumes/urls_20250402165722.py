from django.urls import path
from .views import ResumeViewSet

urlpatterns = [
    path('publish/', ResumeViewSet, name='publish_resume')
]