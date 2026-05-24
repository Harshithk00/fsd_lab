from django.db import models
class Student(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    sub = models.CharField(max_length=20)
    cie = models.IntegerField()
