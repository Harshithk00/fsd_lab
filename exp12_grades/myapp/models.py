from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=20)
    dept = models.CharField(max_length=50)
    grade = models.CharField(max_length=2)
