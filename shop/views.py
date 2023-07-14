from django.shortcuts import render
from .models import Author, Book, CategoryMovie, Movie, Users

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'html/index.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'html/book.html', {'books': books})

def category_list(request):
    categories = CategoryMovie.objects.all()
    return render(request, 'html/categorymovie.html', {'categories': categories})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'html/movie.html', {'movies': movies})

def user_list(request):
    users = Users.objects.all()
    return render(request, 'html/user.html', {'users': users})