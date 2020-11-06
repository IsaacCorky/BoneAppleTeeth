from django.urls import path
from .views import mealSchedulePageView

urlpatterns = [
path("mealschedule/", mealSchedulePageView, name="mealschedule")    
]      