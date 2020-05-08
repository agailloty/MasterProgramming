from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Axel-Cleris Gailloty',
        'title': 'Learning Python',
        'content': 'There are lot of things that can be done with Python',
        'date_posted' : '22/04/2020'
    },
    {
        'author': 'Axel-Cleris Gailloty',
        'title': 'Web development with Python',
        'content': 'I am learning the Django framework for web',
        'date_posted' : '24/04/2020'
    },
    {
        'author': 'Axel',
        'title': 'Data science with Python',
        'content': 'There are quite of good libraries for data science in Python',
        'date_posted' : '28/04/2020'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'people/home.html', context)

def about(request):
    return render(request, 'people/about.html')