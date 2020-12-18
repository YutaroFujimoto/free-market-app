from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'freemarket/index.html')

def login(request):
    return render(request, 'freemarket/login.html')

def information(request):
    return render(request, 'freemarket/information.html')

def change_information(request):
    return render(request, 'freemarket/change_information.html')