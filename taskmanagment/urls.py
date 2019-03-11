from django.urls import path, include
from . import views


app_name = 'taskmanagment'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name="project-list"),
    path('project/create/', views.ProjectCreateView.as_view(), name="project-create"),
    path('project/detail/<int:pk>', views.ProjectDetailView.as_view(), name="project-detail"),
    path('project/update/<int:pk>', views.ProjectUpdateView.as_view(), name="project-update"),
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name="project-delete"),
    path('project/detail/<int:id>/task/<int:pk>', views.TaskDetailView.as_view(), name="task-detail"),
    path('area/create/', views.AreaCreateView.as_view(), name="area-create"),
    path('task/create/', views.TaskCreateView.as_view(), name="task-create"),
    path('task/update/<int:pk>', views.TaskUpdateView.as_view(), name="task-update"),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name="task-delete"),
    path('personel/create/', views.PersonelCreateView.as_view(), name="personel-create"),
    path('personel/delete/<int:pk>', views.PersonelDeleteView.as_view(), name="personel-delete"),
    path('observation/create/', views.ObservationCreateView.as_view(), name="observation-create"),
    path('observation/delete/<int:pk>', views.ObservationDeleteView.as_view(), name="observation-delete"),

]
