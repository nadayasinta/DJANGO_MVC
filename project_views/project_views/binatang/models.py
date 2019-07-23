from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=255)
    species  = models.CharField(max_length=35)
    berat = models.PositiveIntegerField()
    umur = models.PositiveIntegerField()