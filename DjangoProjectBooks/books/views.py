from django.shortcuts import render
from .models import Book, Genre, Author

def books_list(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    authors = Author.objects.all()
    
    context = {
        'books': books,
        'genres': genres,
        'authors': authors,
    }
    
    return render(request, 'books/books_list.html', context)
