from django.db import models

# Create your models here.
class job(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    value = models.IntegerField(default=1)
