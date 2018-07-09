from django.shortcuts import render
from books.models import Book


def index(request):
    books_all = Book.objects.all()
    return render(request, 'index/index.html', {'books_all': books_all})
