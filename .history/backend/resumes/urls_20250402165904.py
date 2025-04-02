from django.urls import path
from .views import ResumeViewSet
resume_list = ResumeViewSet.as_view({'get': 'list', 'post': 'create'})
resume_detail = ResumeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('publish/', resume_list, name='publish_resume'),
    path('publish/<int:pk>/', resume_detail, name='resume_detail'),
]