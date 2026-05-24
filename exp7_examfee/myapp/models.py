from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=20)
    sem = models.IntegerField()
    fee = models.BooleanField(default=False)
