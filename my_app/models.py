from django.db import models
from django.urls import reverse

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    description = models.TextField(max_length=250)
    year = models.IntegerField()


    def __str__(self):
        return self.name    
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})