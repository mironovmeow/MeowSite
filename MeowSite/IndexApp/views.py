from django.shortcuts import render


def index(requests, url):
    return render(requests, f"{url}.html")
