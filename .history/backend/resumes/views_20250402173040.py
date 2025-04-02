from rest_framework.viewsets import generics
from rest_framework.permissions import IsAuthenticated
from .models import Resume
from .tasks import process_resume
from .serializers import ResumeSerializer


class ResumeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        resume = serializer.save(user=self.request.user)
        process_resume(resume.id)
