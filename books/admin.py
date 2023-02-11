from django.contrib import admin
from .models import Book, Category, Author


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', )


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'rating', 'date_created', 'is_public', )
    list_filter = ('is_public', )


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
