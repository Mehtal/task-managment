from django.urls import path, include
from . import views
urlpatterns = [
    path('project', views.ProjectListCreateAPIView.as_view(), name="project-api" )
]
