from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
    {
        'author': 'Clyde',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'

    },
    {
        'author': 'Bryon',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 18, 2018'

    }

]

def home(request):
    content = {
        'posts': posts,

    }
    return render(request, "blog/home.html", content)

def about(request):
    return render(request, "blog/about.html", { "title": "About" })


