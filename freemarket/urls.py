from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('information', views.information, name='information'),
    path('change_information', views.change_information, name='change_information'),
]
