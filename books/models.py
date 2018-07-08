from django.db import models
from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    authors = models.ManyToManyField(Author, blank=True)
    isbn = models.SmallIntegerField()
    publish_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
