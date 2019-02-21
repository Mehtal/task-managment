from django.shortcuts import render
from .serializers import ProjectSerializer
from rest_framework import generics
from taskmanagment.models import (Project, Area, Task, Tool)


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
