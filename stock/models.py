from django.db import models
from django.urls import reverse
# Create your models here.


class Supply(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=11, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    last_modefied = models.DateField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse("stock:update", args=[str(self.id)])

    def __str__(self):
        return self.name

    def get_total(self):
        total = self.quantity * self.unit_price
        return total
