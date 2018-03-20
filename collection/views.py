from django.shortcuts import render
from .forms import BookForm, BookLoanForm
from django import template
from .models import Book, Author
from django.db.models import Q
from django_tables2 import RequestConfig
from .tables import BookTable


def index(request):
    form = BookForm()
    return render(request, 'books/index.html', {'form': form})


def search(request):
    q = request.GET['text_to_search']
    books = Book.objects.filter(Q(isbn__icontains=q) | Q(title__icontains=q))
    authors = Author.objects.filter(Q(name__icontains=q))
    for author in authors:
        books | author.books.all()
    table = BookTable(books)
    RequestConfig(request).configure(table)
    loan_form = BookLoanForm()
    return render(request, 'books/search_results.html', {'table': table, 'loan_form': loan_form})