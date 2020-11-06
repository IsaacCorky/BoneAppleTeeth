from django.urls import path
from .views import shoppingListPageView

urlpatterns = [
path("shoppinglist/", shoppingListPageView, name="shoppinglist")    
]      