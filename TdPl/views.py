from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonSerializer, TaskSerializer
from .models import Person, Task

class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()