from django.shortcuts import render, get_object_or_404
from .models import Book, Category, Author


def index(request):
    categories = Category.objects.all()
    books = Book.objects.filter(is_public=True)

    context = {
        'categories': categories,
        'books': books
    }
    return render(request, 'books/index.html', context)


def authors(request):
    categories = Category.objects.all()
    authors = Author.objects.all()

    context = {
        'categories': categories,
        'authors': authors
    }
    return render(request, 'books/authors.html', context)


def category_detail(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.filter(is_public=True, category=category)

    context = {
        'categories': categories,
        'category': category,
        'books': books
    }
    return render(request, 'books/category.html', context)


def book_detail(request, pk):
    categories = Category.objects.all()
    book = get_object_or_404(Book, pk=pk)

    context = {
        'categories': categories,
        'book': book,
    }
    return render(request, 'books/book_detail.html', context)


