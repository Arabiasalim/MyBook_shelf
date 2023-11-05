from django.db import models


class Bookshelf(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length= 200)
    summary = models.TextField(max_length=200)
    genre = models.CharField(max_length=200)
    publish_date = models.DateField()