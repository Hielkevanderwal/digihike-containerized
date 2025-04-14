from django.db import models

# Create your models here.
class Poster(models.Model):
    poster_name = models.CharField(max_length=200)
    poster_image = models.ImageField()
    poster_date = models.DateField()