from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    fb = models.TextField()
