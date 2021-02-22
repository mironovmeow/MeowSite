from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseForbidden

from MeowSite.MeowSite.secret import vk_secret
from collections import OrderedDict
from urllib.parse import urlencode
from base64 import b64encode
from hashlib import sha256
from hmac import HMAC


def decorate_vk_auth(func, method="GET"):
    def is_valid(request):
        if method == "GET":
            query = request.GET
        elif method == "POST":
            query = request.POST
        else:
            return HttpResponseNotAllowed(method)
        try:
            vk_subset = OrderedDict(sorted(x for x in query.items() if x[0][:3] == "vk_"))
            hash_code = b64encode(HMAC(vk_secret.encode(), urlencode(vk_subset, doseq=True).encode(), sha256).digest())
            decoded_hash_code = hash_code.decode('utf-8')[:-1].replace('+', '-').replace('/', '_')
            if decoded_hash_code:
                return func(request)
            else:
                return HttpResponseForbidden("Auth Error")
        except:
            return HttpResponseForbidden("Auth Error")
    return is_valid


# def decorate_options(func):
#     def decorator(request):
#         if request.method == "OPTIONS":
#             return HttpResponse(code=204)
#         else:
#             return func(request)
#     return decorator
#
#
# @decorate_options
@decorate_vk_auth
def start(request):
    return HttpResponse("Добро пожаловать! Здесь пусто, но скоро что-то будет :)<br><br>"
                        f"Ваш id: {request.GET['vk_user_id']}")
