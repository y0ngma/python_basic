from django.urls import path
from . import views

#127.0.0.1:8000/member/index => index함수 실행하라
#127.0.0.1:8000/member/login
#127.0.0.1:8000/member/join

#127.0.0.1:8000/write => 어디에 글쓰는지 모르니까
#127.0.0.1:8000/board/write 로 만듬
#127.0.0.1:8000/board/list 로 만듬
urlpatterns = [
    # index를 url끝에 치면 views의 index함수를 불러와라
    path('index', views.index, name='index'),
    path('list', views.list, name = 'list'),
    path('member', views.member, name = 'member'),
    path('join', views.join, name = 'join'),
    path('join1', views.join1, name = 'join1'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    
    path('auth_join', views.auth_join, name = 'auth_join'),
    path('auth_login', views.auth_login, name = 'auth_login'),
    path('auth_logout', views.auth_logout, name = 'auth_logout'),
    path('auth_index', views.auth_index, name = 'auth_index'),
    path('auth_edit', views.auth_edit, name = 'auth_edit'),
    path('auth_pw', views.auth_pw, name = 'auth_pw'),
    # 숙제
    path('exam_insert', views.exam_insert, name = 'exam_insert'),
    path('exam_update', views.exam_update, name = 'exam_update'),
    path('exam_delete', views.exam_delete, name = 'exam_delete'),
    path('exam_select', views.exam_select, name = 'exam_select'),
    
    # Script
    path('js_index', views.js_index, name = 'js_index'),
    path('js_chart', views.js_chart, name = 'js_chart'),
    


]