from django.db import models
from .defaults import *

# Create your models here.
class feedback(models.Model):
    user = models.CharField(blank=True, null=True, unique=False ,max_length=LENGTH_BIG, verbose_name="User")
    time = models.CharField(blank=True, null=True, unique=False ,max_length=LENGTH_BIG, verbose_name="Time")
    x = models.CharField(blank=True, null=True, unique=False ,max_length=LENGTH_BIG, verbose_name="X")
    y = models.CharField(blank=True, null=True, unique=False ,max_length=LENGTH_BIG, verbose_name="Y")
    z = models.CharField(blank=True, null=True, unique=False ,max_length=LENGTH_BIG, verbose_name="Z")

    class Meta:
        managed = True
        db_table = 'feedback'
        verbose_name="Feedback"
        verbose_name_plural="Feedback"
    def __str__(self):
        return str(self.id)
