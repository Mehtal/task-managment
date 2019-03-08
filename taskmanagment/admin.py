from django.contrib import admin
from .models import Project, Task, Tool, Area, Observation, Personel
# Register your models here.
admin.site.register(Project)
admin.site.register(Area)
admin.site.register(Task)
admin.site.register(Tool)
admin.site.register(Personel)
admin.site.register(Observation)
