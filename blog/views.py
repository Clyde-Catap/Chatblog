from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.contrib import messages
import time
# Create your views here.
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
    # user_data = User.objects.all()
    # data = {'user': user_data}
    # unique = True

    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your Registration is sucessful!! redirecting in 5 sec'))
            return redirect('/home')
        else:
            messages.warning(request, ('Email or Username already exists!!'))
            return render(request, "blog/signup.html")
            # for user in data['user']:
            #     if user.username == form.cleaned_data['username'] or user.email == form.cleaned_data['email']:
            #         unique = False
            # if unique:
            #     form.save()

            #     time.sleep(5)
            #     return render(request, "blog/signup.html")
            # if not unique:

            #     return render(request, "blog/signup.html")
    else:
        return render(request, "blog/signup.html")

def login(request):
    user_data = User.objects.all
    return render(request, "blog/login.html", {'user': user_data})

