from django.urls import path, include
from . import views


app_name = 'taskmanagment'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name="project-list"),
    path('<int:pk>', views.ProjectDetailView.as_view(), name="project-detail"),
    path('<int:id>/<int:pk>', views.TaskDetailView.as_view(), name="task-detail"),
    path('task/create/', views.TaskCreateView.as_view(), name="task-create"),
    path('area/create/', views.AreaCreateView.as_view(), name="area-create"),
    path('task/update/<int:pk>', views.TaskUpdateView.as_view(), name="task-update"),
    path('project/create/', views.ProjectCreateView.as_view(), name="project-create"),
]
