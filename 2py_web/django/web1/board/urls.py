# 파일명 : board/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # index를 url끝에 치면 views의index함수를 불러와라
    path('write',       views.write,        name='write'),
    path('list',        views.list,         name='list'),
    path('content',     views.content,      name='content'),
    path('edit',        views.edit,         name='edit'),
    path('delete',      views.delete,       name='delete'),
    path('dataframe',   views.dataframe,    name='dataframe'),
    
    path('t2_insert',   views.t2_insert,    name='t2_insert'),
    path('t2_list',     views.t2_list,      name='t2_list'),
    path('t2_update',   views.t2_update,    name='t2_update'),
    path('t2_delete',   views.t2_delete,    name='t2_delete'),
    path('t2_insert_all', views.t2_insert_all, name='t2_insert_all'),
    path('t2_update_all', views.t2_update_all, name='t2_update_all'),

    


]