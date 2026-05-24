from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    job = models.CharField(max_length=50)
    sal = models.IntegerField()
