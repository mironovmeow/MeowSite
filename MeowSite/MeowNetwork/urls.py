from django.urls import path
from MeowNetwork import views

urlpatterns = [
    path('auth/', views.auth, name="auth"),
    path('', views.index, name="index")
]
