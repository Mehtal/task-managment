from rest_framework import serializers
from taskmanagment.models import (Project, Area, Task, Tool)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name"]


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ["id", "name", "project"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "debut", "fin", "area" , "complete", "timestamp"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ["id", "name", "quantity", "unit_price", "task"]

