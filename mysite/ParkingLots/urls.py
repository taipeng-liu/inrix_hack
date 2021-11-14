from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('check/', views.check),
    path('detail/', views.detail)
]
