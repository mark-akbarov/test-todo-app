from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from .serializers import (
    TaskSerializer,
    TaskUpdateSerializer
    )
from .models import  Task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, is_completed=False)

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = TaskSerializer
        elif self.action == 'update':
            self.serializer_class = TaskUpdateSerializer
        elif self.action == 'retrieve':
            self.serializer_class = TaskUpdateSerializer
        else:    
            self.action = TaskSerializer
        return super().get_serializer_class()


class TaskCompletedListView(ListAPIView):
    queryset = Task.objects.filter(is_completed=True)
    serializer_class = TaskSerializer
