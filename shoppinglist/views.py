from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def shoppingListPageView(request) :
    return HttpResponse('<h1>This will be the sshoppinglist view</h1>')  