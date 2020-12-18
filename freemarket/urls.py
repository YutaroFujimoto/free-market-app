from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exhibit_finished', views.exhibit_finished, name='exhibit_finished')
    path('sell_page', views.sell_page, name='sell_page')
]
