from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("SignIn", views.signIn, name="SignIn"),
    path("SignUp", views.signUp, name="SignUp"),
]
