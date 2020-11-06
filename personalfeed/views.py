from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def personalFeedPageView(request) :
    return HttpResponse('This will be the personalfeed page view')  