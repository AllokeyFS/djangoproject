from django.urls import path
from .views import author_list, book_list, category_list, movie_list_90, user_list, new_movies_list, author_list_alive, book_list_90, book_list_00, movie_list_budget_lt_50


urlpatterns = [
    path('author/', author_list, name='author_list'),
    path('book/', book_list, name='book_list'),
    path('category/', category_list, name='category_list'),
    path('movie/', movie_list_90, name='movie_list'),
    path('user/', user_list, name='user_list'),
    path('new_movie/', new_movies_list, name='movie_list'),
    path('author_alive/', author_list_alive, name='author_list_alive'),
    path('book_90/', book_list_90, name='book_list_90'),
    path('book_00/', book_list_00, name='book_list_00'),
    path('movie_budget_lt_50/', movie_list_budget_lt_50, name='movie_list_budget_lt_50'),
]