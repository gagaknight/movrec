from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=200)
    num_stars = models.IntegerField()
    num_users = models.IntegerField()
    avg_rating = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.title
