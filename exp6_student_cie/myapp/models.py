from django.db import models
class Student(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    sub_code = models.CharField(max_length=20)
    cie_marks = models.IntegerField()
