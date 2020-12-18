from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list', views.product_list, name='product_list'),
    path('product_detail', views.product_detail, name='product_detail'),
    path('confirm', views.confirm, name='confirm'),
    path('contact', views.contact, name='contact'),
    path('seller_information', views.seller_information, name='seller_information'),
]
