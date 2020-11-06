from django.urls import path
from .views import loginPageView,loginSuccessPageView

urlpatterns = [
path("", loginPageView, name="login"),
path("successful-login", loginSuccessPageView, name="login"),   
]      