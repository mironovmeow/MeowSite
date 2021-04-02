from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


LOGIN_URL = "/meow_network/auth/"


@require_http_methods(["GET", "POST"])
def auth(request: HttpRequest):
    if request.method == "GET":
        return render(request, "network/auth.html")

    if request.POST.get("logout") == "1":
        logout(request)
        return render(request, "network/auth.html")

    username, password = request.POST.get("username"), request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is None:
        return render(request, "network/auth.html")
    else:
        login(request, user)
        return redirect(request.GET.get("next", '/meow_network/'))


@require_http_methods(["GET"])
@login_required(login_url=LOGIN_URL)
def index(request: HttpRequest):
    return render(request, "network/index.html")
