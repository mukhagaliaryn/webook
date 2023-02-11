from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    slug = models.SlugField(verbose_name='Ключ', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Author(models.Model):
    full_name = models.CharField(verbose_name='Полная имя', max_length=255)
    image = models.ImageField(verbose_name='Изображение', upload_to='books/authors/', blank=True, null=True)
    about = models.TextField(verbose_name='Об автора', blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(verbose_name='Изображение', upload_to='books/images/', blank=True, null=True)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    rating = models.DecimalField(verbose_name='Рейтинг', max_digits=2, decimal_places=1)
    file = models.FileField(verbose_name='Исходный файл', upload_to='books/files/')
    date_created = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(verbose_name='Публикация', default=False)
    authors = models.ManyToManyField(Author, verbose_name='Авторы', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
