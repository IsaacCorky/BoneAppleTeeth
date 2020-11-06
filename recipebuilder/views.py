from django.shortcuts import render
# Create your views here.
# Create your views here.
from django.http import HttpResponse

def recipeDraftPageView(request) :
    return HttpResponse('This will be the recipe draft view')
def currentDraftsPageView(request) :
    return HttpResponse('This will be the current drafts view')
def draftPublishedPageView(request) :
    return HttpResponse('This will be the draft successfully published view')
