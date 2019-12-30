from django.urls import path
from . import views

#127.0.0.1:8000/member/index => index함수 실행하라
#127.0.0.1:8000/member/login
#127.0.0.1:8000/member/join

#127.0.0.1:8000/write => 어디에 글쓰는지 모르니까
#127.0.0.1:8000/board/write 로 만듬
#127.0.0.1:8000/board/list 로 만듬
urlpatterns = [
     path('index', views.index, name='index'),
     path('join', views.join, name = 'join'),
     path('login', views.login, name = 'login')
 ]