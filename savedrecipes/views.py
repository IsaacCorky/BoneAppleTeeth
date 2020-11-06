from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def savedRecipesPageView(request) :
    return HttpResponse('This will be the saved recipespage view')  