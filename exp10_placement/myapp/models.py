from django.db import models
class Student(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
