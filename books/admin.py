from django.contrib import admin
from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('display_authors',)


admin.site.register(Book, BookAdmin)
