from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),
    path('cars/', views.cars_view, name='cars'),
    path('flowers/', views.flowers_view, name='flowers'),
    path('animals/', views.animals_view, name='animals'),
]