from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    date_of_death = models.DateField(null=True, blank=True, verbose_name='Дата смерти')
    description = models.TextField(verbose_name='Биография')
    

    def __str__(self) -> str:
        return f'{self.last_name} - {self.first_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'



class Book(models.Model):
    name = models.CharField(max_length=30,verbose_name='Название книги')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,verbose_name='Автор')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    publication_date = models.DateField(verbose_name='Дата публикации')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class CategoryMovie(models.Model):
    name = models.CharField(max_length=30,unique=True ,verbose_name='Название категории')


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория фильма'
        verbose_name_plural = 'Категория фильмов'


class Movie(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='Фото')
    name = models.CharField(max_length=40, verbose_name='Название фильма')
    category = models.ManyToManyField(CategoryMovie, verbose_name='Категория')
    year_release = models.DateField(verbose_name='Дата релиза')
    company = models.CharField(max_length=30, verbose_name='Компания')
    length = models.IntegerField(verbose_name='Длительность')
    budget = models.DecimalField(max_digits=20,decimal_places=2,verbose_name='Бюджет')
    description = models.TextField(verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    # def category_names(self):
        # return ', '.join([a.name for a in self.category.all()])
    # category_names.short_description = 'Категория фильмов'

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Users(models.Model):

    ROLE_CHOICES = (
        ('user', 'Пользователь'),
        ('admin', 'Админ'),
        ('guest', 'Гость'),
    )
    role=models.CharField(max_length=30,default='guest', choices=ROLE_CHOICES, verbose_name='Роль')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    login = models.CharField(max_length=50, verbose_name='Логин')
    email = models.EmailField(unique=True, verbose_name='Почта')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')


    def __str__(self) -> str:
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


# class Colors(models.Model):
#     actor = 