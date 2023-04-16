from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.landing, name='blog-landing'),
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('profile-name/', views.Profile, name='blog-profile-name'),
    path('signup', views.Signup, name='blog-signup'),
    path('login', views.login, name='blog-login'),
    path('post', views.Post, name='blog-post'),

]