from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from books.models import Author, Book
from .forms import BookForm
import datetime


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            authors = form.cleaned_data['author_input']
            book.authors.set(authors)
            book.save()

            return redirect('books:book_detail', pk=book.pk)
        return render(request, 'books/book_edit.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'books/book_edit.html', {'form': form})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            authors = form.cleaned_data['author_input']
            book.authors.set(authors)
            book = form.save()
            return redirect('books:book_detail', pk=book.pk)
        return render(request, 'books/book_edit.html', {'form': form})
    else:
        authors = book.authors.all()
        form = BookForm(instance=book, initial={'author_input': authors})
        return render(request, 'books/book_edit.html', {'form': form})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def book_manage(request):
    books_all = Book.objects.all()
    return render(request, 'books/book_manage.html', {'books_all': books_all})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('index:index')
