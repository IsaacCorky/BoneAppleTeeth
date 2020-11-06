from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def discoverPageView(request) :
    return HttpResponse('This will be the discover view')  