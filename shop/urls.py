from django.urls import path
from .views import author_list, book_list, category_list, movie_list


urlpatterns = [
    path('author/', author_list, name='author_list'),
    path('book/', book_list, name='book_list'),
    path('category/', category_list, name='category_list'),
    path('movie/', movie_list, name='movie_list'),
    path('user/', movie_list, name='movie_list'),

]