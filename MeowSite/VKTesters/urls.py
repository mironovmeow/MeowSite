from django.urls import path
from VKTesters import views

urlpatterns = [
    path('', views.start),
    path('bug/0/', views.bug0),
    path('bug/1/', views.bug1)
]
