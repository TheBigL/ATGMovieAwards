# import jsonfield
from django.db import models


# Create your models here.

class Database(models.Model):
    Movie_Title = models.CharField(max_length=120)
    Year = models.IntegerField()
    Genre = models.CharField(max_length=100)
    DateReleased = models.CharField(max_length=20)
    imdbRating = models.CharField()
    Runtime = models.CharField(max_length=10)
    Director = models.CharField(max_length=50)
    Writer = models.CharField(max_length=200)
    Actors = models.CharField(max_length=1000)
    Plot = models.TextField()
    Language = models.CharField( max_length=50)
    Country = models.CharField(max_length=100)
    Awards = models.CharField(max_length=50)
    Ratings = models.CharField()
    MetaScore = models.CharField()
    imdbVotes = models.CharField()
    DVD = models.CharField()
    BoxOffice = models.CharField()
    Production = models.CharField()
    Website = models.CharField()
    Response = models.CharField()
    JSONResponse = models.JSONField()
    def _str_(self):
        return self.Movie_Title