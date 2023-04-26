from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout


import time
# Create your views here.
sample_data_1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Cursus turpis massa tincidunt dui ut ornare lectus sit. Nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. Egestas pretium aenean pharetra magna ac placerat. Senectus et netus et malesuada fames. Feugiat in fermentum posuere urna nec. Justo laoreet sit amet cursus sit amet. Elementum curabitur vitae nunc sed velit dignissim sodales ut. Vivamus at augue eget arcu dictum varius duis at consectetur. Pellentesque habitant morbi tristique senectus et netus et malesuada fames. Egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate. A lacus vestibulum sed arcu non odio euismod lacinia. Cras semper auctor neque vitae tempus quam pellentesque."

posts = [
    {
        'author': 'Clyde Bryon Catap',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'

    },
    {
        'author': 'Bryon Catap',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 18, 2018'

    },
    {
        'author': 'Clyde Bryon Catap',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'

    },
    {
        'author': 'Bryon Catap',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 18, 2018'

    },
    {
        'author': 'Clyde Bryon Catap',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'

    },
    {
        'author': 'Bryon Catap',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 18, 2018'

    },
    {
        'author': 'Clyde Bryon Catap',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'

    },
    {
        'author': 'Bryon Catap',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 18, 2018'

    },

]

comments = [
    {
        'author': 'Clyde Catap',
        "title": 'Blog Post 1',
        # should be only 100 chars
        'comment': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'date_commented': "September 6 2203"

    },
    {
        'author': 'Bryon Catap',
        "title": 'Blog Post 1',
        # should be only 100 chars
        'comment': 'Lorem ipsum dolor sit amet, consectetur.',
        'date_commented': "September 6 2203"

    },
]

post = [
    {
        'post': sample_data_1
    }

]


def landing(request):
    return render(request, "blog/landing-content.html")

def home(request):
    content = {
        'posts': posts,
        'comments': comments,
    }

    return render(request, "blog/home.html", content)

def about(request):
    return render(request, "blog/about.html", { "title": "Working", })

def Profile(request):
    content = {
        'posts': posts,
        'comments': comments,
    }

    return render(request, "blog/profile.html", content)
def Signup(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('blog-login')
        else:
            messages.warning(request, ('Email or Username already exists!!'))
            return render(request, "blog/signup.html")
    else:
        return render(request, "blog/signup.html")

def loginPage(request):
    user_data = User.objects.all
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog-home')
    return render(request, "blog/login.html", {'user': user_data})

def Post(request):
    content = {
        'post': post,
    }

    return render(request, "blog/post.html", content)

