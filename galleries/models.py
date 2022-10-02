from django.db import models

# Create your models here.


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    # .......


class Picture(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField()
    # .......