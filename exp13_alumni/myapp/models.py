from django.db import models
class Alumni(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20)
    passing_year = models.IntegerField()
    company = models.CharField(max_length=100)
