from django.shortcuts import render
from django.http import HttpResponse
# insert1
from .models import Item
# select1
from .serializers import ItemSerializer
from rest_framework.renderers import JSONRenderer
import json

def insert1(request):
    # for i in range(1,31,1): 
    #     # bulk_create 사용해서 중도중단시 아예 안올라가게 하자
    #     obj = Item()
    #     obj.name = '연필'+str(i)
    #     obj.price= 1000+i
    #     obj.save()
    return HttpResponse('insert1')

# {'id':'a'} 물품1개
def select1(request):
    if request.method == "GET":
        key = request.GET.get("key", "")
        no = request.GET.get("no", 1)

        if key == "abc":
            obj = Item.objects.get(no=no)
                # DB에서 존재여부 확인이 우선 
            print('------------------------------------1', type(obj), obj)
            serializer = ItemSerializer(obj)
            data = JSONRenderer().render(serializer.data)
            return HttpResponse(data)
        else:
            data = json.dumps({"ret":"key error"})
            return HttpResponse(data)
                # html 없이 가능

# [{'id':'a', 'id':'b'}] 물품2개
def select_m(request):
    if request.method == "GET":
        key = request.GET.get('key', '')
        search = 1

        if key == "abc":
            obj = Item.objects.all()
            serializer = ItemSerializer(obj, many=True)
                # 여러개일 경우 many=True
            data = JSONRenderer().render(serializer.data)

        data = json.dumps({"ret":"key error"})
        return HttpResponse(data)

def select3(request):
    if request.method == "GET":
        key    = request.GET.get('key', '')
        search = request.GET.get('search','')
        num= int(request.GET.get('num', 1))

        if key == "abc":
            obj = Item.objects.filter(name__contains=str(search))[0:num]
                # SELECT*FROM API_MEMBER 
                # WHERE ID LIKE  "%%'''+str(search)+'''%%" ORDER BY NO DESC
            serializer = ItemSerializer(obj, many=True)
            data = JSONRenderer().render(serializer.data)
            return HttpResponse(data)
        else:
            data = json.dumps({"ret":"key error"})
            return HttpResponse(data)






    sql='''
        SELECT*FROM API_MEMBER 
        WHERE ID LIKE  "%%'''+str(search)+'''%%" ORDER BY NO DESC
    '''
    # cursor.execute(sql, search)
    # search = cursor.fetchall()
    
    # rows = list(Table2.objects.all().values("no", 'name', 'kor'))[0:10]
