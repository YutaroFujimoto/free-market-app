from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={
        "articles":Article.objets.all()
    }
    return render(request, 'freemarket/index.html')
    
def product_list(request):
    return render(request, 'freemarket/product_list.html')

def product_detail(request):
    return render(request, 'freemarket/product_detail.html')

def confirm(request):
    return render(request, 'freemarket/confirm.html')

def contact(request):
    return render(request, 'freemarket/contact.html')

def seller_information(request):
    return render(request, 'freemarket/seller_information.html')

def login(request):
    return render(request, 'freemarket/login.html')

def information(request):
    return render(request, 'freemarket/information.html')

def change_information(request):
    return render(request, 'freemarket/change_information.html')

def exhibit_finished(request):
    return render(request, 'freemarket/exhibit_finished.html')

def sell_page(request):
    return render(request, 'freemarket/sell_page.html')