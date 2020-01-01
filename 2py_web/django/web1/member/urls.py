from django.urls import path
from . import views

#127.0.0.1:8000/member/index => index함수 실행하라
#127.0.0.1:8000/member/login
#127.0.0.1:8000/member/join

#127.0.0.1:8000/write => 어디에 글쓰는지 모르니까
#127.0.0.1:8000/board/write 로 만듬
#127.0.0.1:8000/board/list 로 만듬
urlpatterns = [
    # index를 url끝에 치면 views의index함수를 불러와라
    path('index', views.index, name='index'),
    path('list', views.list, name = 'list'),
    path('member', views.member, name = 'member'),
    path('join', views.join, name = 'join'),
    path('join1', views.join1, name = 'join1'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout')



]