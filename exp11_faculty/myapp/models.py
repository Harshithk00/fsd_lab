from django.db import models
class Faculty(models.Model):
    fid = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
