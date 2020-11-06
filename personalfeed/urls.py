from django.urls import path
from .views import personalFeedPageView

urlpatterns = [
path("personalfeed/", personalFeedPageView, name="personalfeed")    
]      