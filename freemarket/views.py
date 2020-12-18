from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
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
