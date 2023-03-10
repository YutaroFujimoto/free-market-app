from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path('userlogin', views.userlogin, name='userlogin'),
    path('information', views.information, name='information'),
    path('show_information', views.show_information, name='show_information'),
    path('<int:userdata_id>', views.information_detail, name='information_detail'),
    path('new_information', views.new_information, name='new_information'),
    path('<int:article_id>/', views.detail, name = 'detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
