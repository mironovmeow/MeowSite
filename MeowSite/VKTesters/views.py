from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from VKTesters.models import Report
from MeowSite.secret import vk_secret
from collections import OrderedDict
from urllib.parse import urlencode
from base64 import b64encode
from hashlib import sha256
from hmac import HMAC


def is_valid(request):
    query = request.GET
    try:
        vk_subset = OrderedDict(sorted(x for x in query.items() if x[0][:3] == "vk_"))
        hash_code = b64encode(HMAC(vk_secret.encode(),
                                   urlencode(vk_subset, doseq=True).encode(),
                                   sha256).digest())
        decoded_hash_code = hash_code.decode('utf-8')[:-1].replace('+', '-').replace('/', '_')
        status = query["sign"] == decoded_hash_code
    except:
        return False
    else:
        return status


def my_login_required(func):
    def decorator(request):
        if request.user.is_authenticated:
            return func(request)
        else:
            return redirect("/vk_app/")
    return decorator


def start(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        if is_valid(request):
            user = authenticate(username=request.GET["vk_user_id"], password="")
            if user is None:
                user = User.objects.create_user(username=request.GET["vk_user_id"], password="")
            login(request, user)
            print(request.user.is_authenticated)
            return render(request, "vk_app.html")
        else:
            return HttpResponseForbidden("Auth Error")
    else:
        return render(request, "vk_app.html")


@my_login_required
def bug0(request):
    try:
        Report.objects.get(user=request.user, bug_id=1)  # Checking Report
        # todo: Make messages
        return redirect("/vk_app/")
    except Report.DoesNotExist:
        Report.objects.create(user_id=request.user.id, bug_id=1)
        return render(request, "bug0.html")


@my_login_required
def bug1(request):
    return HttpResponse('В процессе...<a href="/vk_app/"><button>Вернуться назад.</button></a>')
