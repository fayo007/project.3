from django.shortcuts import render

from django.shortcuts import render 
from django.http import HttpResponse
from .models import *


def get_service(request):
    services = Service.objects.all()
    return HttpResponse('Malumot olindi')

def create_service(request):
    service = Service.objects.create(title = 'Phone')
    return HttpResponse('Malumot yaratilindi')

def update_service(request):
    service = Service.objects.get(id=1)
    service.title='Tv'
    service.save()
    return HttpResponse("Ma'lumot muvaffaqiyatli yangilandi")

def delete_service(request):
    service = Service.objects.get(id=1)
    service.delete()
    return HttpResponse("Ma'lumot bazadan o'chirildi")



def get_user(request):
    user = User.objects.all()
    return HttpResponse('Malumot olindi')

def create_user(request):
    user = User.objects.create(name='Fayozbek',email = 'fayo.gmail.com' , phone ='998935678989')
    return HttpResponse('Malumot yaratilindi')

def update_user(request):
    user = User.objects.get(id=1)
    user.name='Ismoil'
    user.save()
    return HttpResponse("Ma'lumot muvaffaqiyatli yangilandi")

def delete_user(request):
    user = User.objects.get(id=1)
    user.delete()
    
    return HttpResponse("Ma'lumot bazadan o'chirildi")




def get_price(request):
    price = Price.objects.all()
    return HttpResponse('Malumot olindi')

def create_price(request):
    price = Price.objects.create(status='$', price = '20000' , is_active=True)
    return HttpResponse('Malumot yaratilindi')

def update_price(request):
    price = Price.objects.get(id=1)
    price.price='50000'
    price.save()
    return HttpResponse("Ma'lumot muvaffaqiyatli yangilandi")

def delete_price(request):
    price = Price.objects.get(id=1)
    price.delete()
    
    return HttpResponse("Ma'lumot bazadan o'chirildi")




def get_product(request):
    product = Product.objects.all()
    return HttpResponse('Malumot olindi')

def create_product(request):
    product = Product.objects.create(title = 'smartfonlar')
    return HttpResponse('Malumot yaratilindi')

def update_product(request):
    product = Product.objects.get(id=1)
    product.title='Televizorlar'
    product.save()
    return HttpResponse("Ma'lumot muvaffaqiyatli yangilandi")

def delete_product(request):
    product = product.objects.get(id=1)
    product.delete()
    return HttpResponse("Ma'lumot bazadan o'chirildi")
