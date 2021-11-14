from django.urls import path
from . import views

urlpatterns = [
    path('findPrkg/', views.findPrkg),
    path('', views.index, name='index')
]
