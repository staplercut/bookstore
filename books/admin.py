from django.contrib import admin
from books.models import Book
from books.models import Author


class AuthorAdmin(admin.ModelAdmin):
    filter_horizontal = ('Book',)


admin.site.register(Book)
admin.site.register(Author)
