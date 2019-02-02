from django.contrib import admin
from .models import Project, Task, Tool, Area
# Register your models here.
admin.site.register(Project)
admin.site.register(Area)
admin.site.register(Task)
admin.site.register(Tool)
