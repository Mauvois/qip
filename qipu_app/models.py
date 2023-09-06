from django.db import models

# Create your models here.


class timescales (models.Model):
    century = models.CharField(max_length=50)
    decade = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    hour = models.CharField(max_length=50)
    minute = models.CharField(max_length=50)
    second = models.CharField(max_length=50)
