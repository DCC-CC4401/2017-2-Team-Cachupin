import datetime

from django.db import models
from django.utils import timezone

class Animal(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=200)
    commune = models.CharField(max_length=100)
    region = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    type = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()