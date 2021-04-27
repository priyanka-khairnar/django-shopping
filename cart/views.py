from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cart(request):
    return HttpResponse('Cart view')


def checkout(request):
    return HttpResponse('Checkout view')