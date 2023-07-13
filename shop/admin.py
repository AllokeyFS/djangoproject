from django.contrib import admin
from .models import Author, Book, CategoryMovie, Movie, Users

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death', 'description', )
    search_fields = ('first_name', 'last_name',)
    list_display_links = ('id', 'first_name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'author','in_stock' ,'publication_date')
    list_filter = ('in_stock', 'publication_date', 'author')
    search_fields = ('name','author__first_name')
    list_display_links = ('id', 'author',)
    list_editable = ('in_stock',)
    autocomplete_fields = ('author',)


class CategoryMovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )
    search_fields = ('name', )

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'name', 'category', 'year_release', 'company', 'length', 'budget', 'description', )
    list_filter = ('category', 'company',)
    readonly_fields = ('image',)
    search_fields = ('name', )
    list_display_links = ('id', 'name', )
    autocomplete_fields = ('category', )

# @admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'login', 'email', 'date', )


# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)
admin.site.register(CategoryMovie,CategoryMovieAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Users, UsersAdmin)