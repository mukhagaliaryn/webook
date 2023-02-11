from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug>/', views.category_detail, name='category_detail'),
    path('book/<pk>/', views.book_detail, name='book_detail'),
    path('authors/', views.authors, name='authors')
]