from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list', views.product_list, name='product_list'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('confirm', views.confirm, name='confirm'),
    path('contact', views.contact, name='contact'),
    path('seller_information', views.seller_information, name='seller_information'),
    path('exhibit_finished', views.exhibit_finished, name='exhibit_finished'),
    path('sell_page', views.sell_page, name='sell_page'),
    path('login', views.login, name='login'),
    path('information', views.information, name='information'),
    path('change_information', views.change_information, name='change_information'),
    path('new_information', views.new_information, name='new_information'),
    path('<int:article_id>/', views.detail, name = 'detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


