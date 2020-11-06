from django.urls import path
from .views import savedRecipesPageView

urlpatterns = [
path("savedrecipes/", savedRecipesPageView, name="savedrecipe")    
]      