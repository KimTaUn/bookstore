from functools import partial
from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='bookList'),
    path('<int:pk>', views.BookDetailView.as_view(), name='bookDetail'),
    path('<int:id>/review', views.review, name="book.review"),
    path('<str:author>', views.author, name='author.book')
]
