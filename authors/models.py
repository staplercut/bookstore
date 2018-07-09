from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def display_books(self):
        return self.name + ': ' + ', '.join([book.title for book in self.book_set.all()])

    display_books.short_description = 'Authors'
    display_books.allow_tags = True

    def __str__(self):
        return self.name
