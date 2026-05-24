from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)
