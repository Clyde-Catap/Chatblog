from django.shortcuts import render
from django.http import HttpResponse
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

    }

]

recent_comments = [
    {
        'author': 'Bryon Catap',
        "title": 'Blog Post 1',
        # should be only 100 chars
        'comment': 'comment',
        'date_commented': "September 6 2203"

    },
    {
        'author': 'Bryon Catap',
        "title": 'Blog Post 1',
        # should be only 100 chars
        'comment': 'comment',
        'date_commented': "September 6 2203"

    },
]

def home(request):
    content = {
        'posts': posts,
        "comments": recent_comments,

    }
    return render(request, "blog/home.html", content)

def about(request):
    return render(request, "blog/about.html", { "title": "About" })


