from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('profile-name/', views.Profile, name='profile-name')
]