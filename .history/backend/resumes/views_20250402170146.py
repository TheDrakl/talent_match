from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Resume
from .tasks import process_resume
from .serializers import ResumeSerializer


class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def perform_create(self, serializer):
        resume = serializer.save(user=self.request.user)
        process_resume(resume.id)
