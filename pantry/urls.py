from django.urls import path
from .views import pantryPageView

urlpatterns = [
path("pantry/", pantryPageView, name="pantry")    
]      