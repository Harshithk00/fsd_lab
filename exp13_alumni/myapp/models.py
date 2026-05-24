from django.db import models
class Alumni(models.Model):
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=20)
    year = models.IntegerField()
    company = models.CharField(max_length=50)
