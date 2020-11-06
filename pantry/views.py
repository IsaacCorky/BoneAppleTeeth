from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pantryPageView(request) :
    return HttpResponse('<ul>This will be the pantry page view</ul>')