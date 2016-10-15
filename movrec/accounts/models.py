from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ratings(models.Model):
    userId = models.IntegerField()
    movieId = models.IntegerField()
    rating = models.IntegerField()
    
    def __str__(self):
        return "userId: " + str(self.userId) + " " + "movieId: " + str(self.movieId) + " rating: " + str(self.rating)
