from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=1000)
    first_published_year = models.IntegerField(null=True, default=None)
    rating = models.FloatField(null=True, default=None)


class Edition(models.Model):
    publish_date = models.DateField()
    publisher = models.CharField(max_length=1000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language = models.CharField(max_length=1000)


class Author(models.Model):
    name = models.CharField(max_length=1000)
    birth_date = models.DateField(null=True, default=None)
    death_date = models.DateField(null=True, default=None)
    books = models.ManyToManyField(Book)
