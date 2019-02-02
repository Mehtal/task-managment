from django.contrib import admin
from django.urls import path, include
from taskmanagment import views
from stock import views as stock_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.ProjectView ),
    path('', views.ProjectListView.as_view(), name="project_list"),
    path('<int:pk>', views.ProjectDetailView.as_view(), name="project-detail"),
    path('<int:id>/<int:pk>', views.TaskDetailView.as_view(), name="task-detail"),
    path('task/create/', views.TaskCreateView.as_view(), name="task-create"),
    path('task/update/<int:pk>', views.TaskUpdateView.as_view(), name="task-update"),
    path('project/create/', views.ProjectCreateView.as_view(), name="project-create"),
    path('restock/<int:pk>', stock_views.add_supply, name="restock"),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
