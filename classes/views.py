from rest_framework import viewsets

from .models import Class
from .permissions import IsClassTeacherOrReadOnly
from .serializers import ClassSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsClassTeacherOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
