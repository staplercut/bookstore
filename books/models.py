from django.db import models
from authors.models import Author
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    authors = models.ManyToManyField(Author, blank=True)
    isbn = models.SmallIntegerField()
    publish_date = models.DateField(default=timezone.now, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def display_authors(self):
        return self.title + ': ' + ', '.join([author.name for author in self.authors.all()])

    display_authors.short_description = 'Books'
    display_authors.allow_tags = True

    def __str__(self):
        return self.title
