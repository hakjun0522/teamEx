from django.db import models
import os


# 웹크롤링
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
class Song1(models.Model):
    title1 = models.CharField(max_length=50)
    artist1 = models.CharField(max_length=50)
    album1 = models.CharField(max_length=50)

class Song2(models.Model):
    title2 = models.CharField(max_length=50)
    artist2 = models.CharField(max_length=50)
    album2 = models.CharField(max_length=50)


# Create your models here.
