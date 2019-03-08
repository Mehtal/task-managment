from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150, blank=True, null=True)
    last_modefied = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task:project-detail', args=[str(self.id)])


class Area(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='areas')

    def __str__(self):
        return "%s %s" % (self.project.name, self.name)


class Task(models.Model):
    name = models.CharField(max_length=100)
    debut = models.DateField()
    fin = models.DateField()
    start = models.BooleanField(default=False,)
    complete = models.BooleanField(default=False)
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name='tasks')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.name, self.area.name)

    def get_absolute_url(self):
        return reverse('task:task-detail', args=[str(self.area.project.id), str(self.id,)])

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
                return "tu as fini {} jours en avance".format(timedelta.days)
            if self.fin < self.timestamp.date():
                timedelta = self.timestamp.date() - self.fin
                return "tu as fini {} jours de retard".format(timedelta.days)
            else:
                return "tu as fini à l'heure"
        if self.complete == False:
            if self.timestamp.date() < self.fin:
                timedelta = self.fin - self.timestamp.date()
                return "{} jours restants pour achever la tâche".format(timedelta.days)
            if self.fin < self.timestamp.date():
                timedelta = self.timestamp.date() - self.fin
                return "vous avez {} jours de retard".format(timedelta.days)


class Personel(models.Model):
    name = models.CharField(max_length=25)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='personels')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task:task-detail', args=[str(self.task.area.project.id), str(self.task.id,)])


class Observation(models.Model):
    name = models.CharField(max_length=150)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='observations')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task:task-detail', args=[str(self.task.area.project.id), str(self.task.id,)])


class Tool(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=11, decimal_places=2)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='tools')
    # project = models.ForeignKey(
    #     Project, on_delete=models.CASCADE, related_name='tools')

    def __str__(self):
        return self.name

    def get_total(self):
        total = self.quantity * self.unit_price
        return total
