from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


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
    # new_information.htmlで投稿(Submit)した場合
    if (request.method == 'POST'):
        data = Userdata(password = request.POST["password"], title = request.POST["title"],)
        data.save()
        # information.htmlへ
        context = {"data" : data,}
        return render(request, 'freemarket/detail.html', context)    



def change_information(request):
    return render(request, 'freemarket/change_information.html')


def exhibit_finished(request):
    return render(request, 'freemarket/exhibit_finished.html')

def sell_page(request):
    if (request.method=='POST'):
        sell_name=
    return render(request, 'freemarket/sell_page.html')

def new_information(request):
    return render(request, 'freemarket/new_information.html')

def detail(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	if request.method == 'POST':
		comment = Comment(article=article, text=request.POST['text'])
		comment.save()

	context = {
		'article': article,
		'comments': article.comments.order_by('-posted_at')
	}
	return render(request, "freemarket/detail.html", context)
