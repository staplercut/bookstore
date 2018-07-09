from books.models import Author
from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('display_books',)


admin.site.register(Author, AuthorAdmin)
