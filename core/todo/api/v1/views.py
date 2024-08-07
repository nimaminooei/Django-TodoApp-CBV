from rest_framework.response import Response
from todo.models import Tasks
from .serializers import TaskSerializer
from rest_framework import permissions , generics
from django.shortcuts import get_object_or_404

class ApiTaskView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    def get_queryset(self, *args, **kwargs):
        return (super().get_queryset(*args, **kwargs).filter(user=self.request.user))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ApiTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "todo_id"

    def get_object(self, queryset=None):
        obj = get_object_or_404(Tasks , pk=self.kwargs["todo_id"])

        return obj

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()
        return Response({"detail": "successfully removed"})

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)