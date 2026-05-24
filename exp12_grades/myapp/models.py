from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    grade = models.CharField(max_length=2)
