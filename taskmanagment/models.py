from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])


class Area(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='areas')

    def __str__(self):
        return "%s %s" % (self.name, self.project.name)


class Task(models.Model):
    name = models.CharField(max_length=100)
    debut = models.DateField()
    fin = models.DateField()
    complete = models.BooleanField(default=False)
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name='tasks')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.name, self.area.name)

    def get_status(self):
        if self.debut <= timezone.now().date() and self.fin >= timezone.now().date() and self.complete == False:
            self.status = "EN COURS"
        elif self.debut >= timezone.now().date():
            self.status = "NON COMMENCE"
        elif self.complete == True:
            self.status = "ACHEVER"
        else:
            self.status = "EN RETARD"
        return self.status

    def get_task_length(self):
        task_length = self.fin - self.debut
        return task_length.days

    def complition_ratio(self):
        if self.status != "NON COMMENCE":
            task_length = self.fin - self.debut
            task_length = task_length.days
            timedelta = timezone.now().date() - self.debut
            timedelta = timedelta.days
            ratio = int(timedelta * 100 / task_length)
            if self.status == "ACHEVER":
                ratio = 100
            return ratio
        else:
            return 0

    def task_info(self):
        if self.complete == True:
            if self.timestamp.date() < self.fin:
                timedelta = self.fin - self.timestamp.date()
                return "you've finished {} days early".format(timedelta.days)
            if self.fin < self.timestamp.date():
                timedelta = self.timestamp.date() - self.fin
                return "you've finished {} days late".format(timedelta.days)
            else:
                return "you've finished on timedelta"

    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.area.project.id), str(self.id,)])


class Tool(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='tools')

    def __str__(self):
        return self.name
