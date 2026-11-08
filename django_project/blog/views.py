from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Storonskyi Sviatoslav',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 8 2026'
    },
    {
        'author': 'John Smith',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 9 2026'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
