from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('index page')

def login(request):
    return ''

def join(request):
    return ''