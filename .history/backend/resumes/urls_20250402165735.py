from django.urls import path
from .views import ResumeViewSet

urlpatterns = [
    path('publish/', ResumeViewSet.as_view, name='publish_resume')
]