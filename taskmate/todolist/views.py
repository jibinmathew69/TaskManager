from django.shortcuts import render
from django.http import HttpResponse

def todolist(request):
    context = {
        'welcome_text' : 'Welcome to Todolist'
    }
    return render(request, 'todolist.html', context)


def contact(request):
    context = {
        'welcome_text' : 'Welcome to contact us'
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'welcome_text' : 'Welcome to about us'
    }
    return render(request, 'about.html', context)