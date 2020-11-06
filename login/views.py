from django.shortcuts import render
from django.http import HttpResponse

def loginPageView(request) :
    return HttpResponse('This will be the login view')  

def loginSuccessPageView(request) :
    return HttpResponse('This will be the login success view')  

def handler404(request):    
    return render('<p>big guys</p>', status =  404) 

def handler500(request):    
    return render(request, '500.html', status=500)
    docstring
    """
    raise NotImplementedError"""
