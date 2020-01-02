## 게시판 글쓰기 만들기
- write.html
### url 연결
    - path('write', views.write, name='write'),

    C:\Users\admin\Documents\python_basic\2py_web\django\web1\board\urls.py
    # 파일명 : board/urls.py
        ``` 
        $$$
        from django.urls import path
        from . import views

        urlpatterns = [
            # index를 url끝에 치면 views의index함수를 불러와라
            path('write', views.write, name='write'),
        ]
        $$$
        ```
### urls 추가         
    - path('board/', include('board.urls')),

    C:\Users\admin\Documents\python_basic\2py_web\django\web1\web1\urls.py

        ```
        $$$
            """web1 URL Configuration

            The `urlpatterns` list routes URLs to views. For more information please see:
                https://docs.djangoproject.com/en/3.0/topics/http/urls/
            Examples:
            Function views
                1. Add an import:  from my_app import views
                2. Add a URL to urlpatterns:  path('', views.home, name='home')
            Class-based views
                1. Add an import:  from other_app.views import Home
                2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
            Including another URLconf
                1. Import the include() function: from django.urls import include, path
                2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
            """

        
        from django.contrib import admin
        from django.urls import path, include
        #127.0.0.1:8000/admin
        #127.0.0.1:8000/member
        #127.0.0.1:8000/board/

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('member/', include('member.urls')),
            path('board/', include('board.urls')),
        ]
        $$$
        ```   
### 함수 정의
    C:\Users\admin\Documents\python_basic\2py_web\django\web1\board
    views.py
        ```
        $$$
        # board/views.py
        from django.shortcuts import render, redirect
        from django.http import HttpResponse
        from django.views.decorators.csrf import csrf_exempt
        from django.db import connection 

        @csrf_exempt
        def write(request):
            if request.method == 'GET':
                return render(request, 'board/write.html')
        $$$
        ```

    C:\Users\admin\Documents\python_basic\2py_web\django\web1\templates\board
    write.html
        ```
        $$$
        $$$
        ```