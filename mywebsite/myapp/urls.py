from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('about/', views.about, name='about'),
    path ('CreateMobile/', views.CreateMobile, name='Create'),
    path ('update/<int:pk>', views.update, name='update'),
    path ('read/<int:pk>', views.read, name='read'),
    path ('delete/<int:pk>', views.delete, name='delete'),
    path ('login/', views.loginPage, name='login'),
    path ('logout/', views.logoutUser, name='logout'),
    path ('signup/', views.registerPage, name='register'),
]