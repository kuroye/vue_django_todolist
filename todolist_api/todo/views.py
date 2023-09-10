from email.policy import default
from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from .serializers import TodoSerializer, TodoUpdateSerializer

from todo.models import Todo

# Create your views here.


class TodoView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request):
        id =int( request.GET.get("id") )
        # print("I AM USER ID ", id)
        todo_data = Todo.objects.filter(user=id)
        # todo_data = self.get_queryset()
        ser = TodoSerializer(todo_data, many=True)
        return Response(ser.data)

class TodoRetrieveDeleteView(generics.RetrieveDestroyAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoRetrieveUpdateView(generics.RetrieveUpdateAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoUpdateSerializer