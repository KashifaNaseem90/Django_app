from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path('bookstore', views.landingpage, name='bookstore'),
    path('', views.index, name='home'),
    path('books', views.listOfBooks, name='books'),
    path('cont', views.cont, name='cont'),
]
