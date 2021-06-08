from two_factor.urls import urlpatterns as tf_urls
from django.urls import path, include
from . import views

urlpatterns = [
    path("", include(tf_urls)),
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
]
