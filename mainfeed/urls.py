from django.urls import path
from .views import mainPageView

urlpatterns = [
path("mainfeed", mainPageView, name="index")    
]                  
            