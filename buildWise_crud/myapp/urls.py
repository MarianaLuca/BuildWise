from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_list, name='book_list'),
    path('book/add/', views.book_create, name='book_create'),
    path('book/<int:pk>/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
