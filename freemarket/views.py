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

def login(request):
    return render(request, 'freemarket/login.html')

def information(request):
    return render(request, 'freemarket/information.html')

def change_information(request):
        # create.htmlで投稿(Submit)した場合
    if (request.method == 'POST'):
        newblog = {
            'id': 10,
            'number': request.POST['number'],
            'password': request.POST['password'],
            'address': request.POST['address'],
            'mailaddress': request.POST['mailaddress'],
            'lineid': request.POST['lineid'],
            'twitterid': request.POST['twitterid'],
            'body': request.POST['text'],
            'posted_at': timezone.now            
        }
        # detail.htmlへ
        return render(request, 'blog/detail.html', newblog)    
    context = {
        'articles': [
            {   
            'id': 1,
            'title': 'Post 01',
            'body': 'text post.\nLorem ipsum dolor sit amet, \nconsecterur adipiscing elit, \n sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n',
            'posted_at': timezone.now
            }    
        ]
    }
    return render(request, 'blog/index.html', context)

def exhibit_finished(request):
    return render(request, 'freemarket/exhibit_finished.html')

def sell_page(request):
    return render(request, 'freemarket/sell_page.html')

def new_information(request):
    return render(request, 'freemarket/new_information.html')
