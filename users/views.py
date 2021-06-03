from django.shortcuts import render
from users.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from django.shortcuts import redirect, render

# Create your views here.


def dashboard(request):
    return render(request, "dashboard.html")


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            print(form)
            return redirect(reverse("register"))