from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mainPageView(request) :
    return HttpResponse('This will be the main view')  