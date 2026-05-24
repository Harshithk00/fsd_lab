from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_hired = models.DateField()
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()
