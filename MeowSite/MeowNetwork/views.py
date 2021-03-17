from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


@require_http_methods(["GET", "POST"])
# @login_required()
def auth(request: HttpRequest):
    if request.method == "GET":
        return render(request, "auth.html")

    login, password = request.POST.get("login"), request.POST.get("login")

