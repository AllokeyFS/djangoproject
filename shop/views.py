from django.shortcuts import render
from .models import Author, Book, CategoryMovie, Movie, Users
from datetime import date

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'html/index.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'html/book.html', {'books': books})

def category_list(request):
    categories = CategoryMovie.objects.all()
    return render(request, 'html/categorymovie.html', {'categories': categories})

def movie_list_90(request):
    movies = Movie.objects.filter(year_release__lt = date(2000, 1, 1), year_release__gt = date(1990,1,1))
    return render(request, 'html/movie.html', {'movies': movies})

def user_list(request):
    users = Users.objects.all()
    return render(request, 'html/user.html', {'users': users})

def new_movies_list(request):
    movies = Movie.objects.filter(year_release__gte = date(2020,1,1))
    return render(request, 'html/new_movie.html', {'movies': movies})