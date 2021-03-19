from django.apps import AppConfig


class VktestersConfig(AppConfig):
    name = 'VKTesters'

    # For saving cookies cross VK iFrame  (test it!)
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SAMESITE = 'None'
    SESSION_SAVE_EVERY_REQUEST = True
