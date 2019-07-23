from django.db import models

# Create your models here.
class Mentor(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=35)
    experience = models.PositiveIntegerField()
    comment = models.TextField()
    photo =  models.URLField(max_length=255)

class Mentee(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    photo =  models.URLField(max_length=255)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content =  models.TextField()
    date_create = models.DateField()
    photo =  models.URLField(max_length=255)
