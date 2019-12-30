from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'member/index.html')
    #return HttpResponse('index page <hr />') 처럼 하던 불편사항 개선
def login(request):
    return ''

def join(request):
    return ''