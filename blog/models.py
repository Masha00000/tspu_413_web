from django.db import models

# Create your models here.
class Articl(models.Model):
    title = models.CharField(
        max_length=255,
        )
    text = models.CharField(
        max_length=1000,
        )
