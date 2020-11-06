from django.urls import path
from .views import discoverPageView

urlpatterns = [
path("discover", discoverPageView, name="discover")    
]                  
         