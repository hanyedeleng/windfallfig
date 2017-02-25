from django.db import models
import datetime

# Create your models here.


# Movie
class Movie(models.Model):
    # name = movie name + year, make it unique
    name = models.CharField(max_length=128, unique=True) 

    # date info
    pubdate = models.DateTimeField(default=datetime.date.today)

    # poster link is the path to the poster(image) file
    posterpath = models.CharField(max_length=128)

    # basic information of a movie, e.g. director, writer, stars
    basicinfo = models.CharField(max_length=256)

    # synopsis
    synopsis = models.CharField(max_length=512)
    relatedlinks = models.CharField(max_length=256)

    def __str__(self):
        return self.name
