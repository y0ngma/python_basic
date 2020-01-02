# board/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection 

@csrf_exempt
def write(request):
    if request.method == 'GET':
        return render(request, 'board/write.html')