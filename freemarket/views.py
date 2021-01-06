from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .models import Userdata

# Create your views here.
def index(request):
    return render(request, 'freemarket/index.html')
    
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'freemarket/product_list.html', context)

def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        related_products = Product.objects.filter(genre=product.genre)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    context = {
		'product': product,
        'related_products': related_products,
	}
    return render(request, 'freemarket/product_detail.html', context)

def confirm(request):
    return render(request, 'freemarket/confirm.html')

def contact(request):
    return render(request, 'freemarket/contact.html')

def seller_information(request):
    return render(request, 'freemarket/seller_information.html')

def login(request):
    return render(request, 'freemarket/login.html')

def information(request):
    # 情報が入力された場合
    if request.method == 'POST':
        data = Userdata(title = request.POST["title"], password = request.POST["password"], name = request.POST["name"], icon = request.POST["icon"], address = request.POST["address"], mail = request.POST["mail"], line = request.POST["line"], twitter = request.POST["twitter"], text = request.POST["text"],)
        data.save() # データベースの更新
        context = {'data': data}
        return render(request, 'freemarket/detail.html', context) 
    else:
        data = Userdata.objects.all() # データの取り出し
        context = {"data" : data,} # 辞書型
        return render(request, 'freemarket/information.html', context) # viewの表示



def change_information(request):
    return render(request, 'freemarket/change_information.html')


def exhibit_finished(request):
    return render(request, 'freemarket/exhibit_finished.html')

def sell_page(request):
    return render(request, 'freemarket/sell_page.html')

def new_information(request):
    return render(request, 'freemarket/new_information.html')

def detail(request):
    return render(request, "freemarket/detail.html")