# Django WEB 
## Index
- 개발 환경
    - 파이썬, 장고, 데이터 베이스
        1. 파이썬 설치
        2. 장고 설치
        3. 데이터베이스 설치
                - SQLite(추천)
            - 메모리에 상주하는 프로세스 없이 파일 하나에 데이터베이스를 저장 
        4. 장고 프로젝트 만들기
            - Step01
                - 터미널 => ``` $ django-admin.py startproject 프로젝트이름```
                - 현재 디렉터리에 '프로젝트이름'을 만들고 기본파일 자동 설치
            - Step02
                - Web 요소 구성하기  
                - 어플리케이션 생성 (여러개 생성 가능)   
                    - Board, Member 앱 생성     
                - Django 서버 구동(http://127.0.0.1:8000/) 
            - Step 03
                - Member 기능 추가 
                    - INDEX, LOGIN, Singin 페이지 등등 생성

## Why Django

1. 구성요소들 간의 긴밀한 통합 
    - 장고는 각 요소가 긴밀하게 통합되어 있음  
    - 모든 부분이 통합적(integration)이며 동작이 빠르다. 그리고 재사용 가능하게 설계   
1. 객체 관계의 매핑     
    - 객체 관계의 매핑(Object-Relational Mapper, ORM))이란     
        : 데이터 베이스 엔진과 데이터 모델을 연결시키는 다리와 같은 역활     
    - 다양한 데이터 베이스를 지원, 유연한 데이터 베이스 시스템 변경     
    - 장고는 데이터베이스를 일관성 있게 추상화해서 단일한 API로 여러 데이터베이스를 사용      

1. 간단한 URL 주소 설계    
    - 강력하고 유연한 URL 주소 디자인  
         - URL주소 형태를 직접 결정 
    - 파이썬 함수를 각 주소 형태와 직접 연결 
        - 일반 사용자와 검생 엔진 각각에 알맞는 결과를 제공 

1. 자동으로 구성되는 관리자 화면 
    - 장고는 실행하는 순간 미리 내장되어 있는 관리자 화면 제공 
    - 여러 어플리케이션의 데이터를 쉽게 관리, 재구성 

1. 풍부한 개발 환경
    - 가벼운 웹 서버를 포함하고 있고 개발뿐아니라 테스트 용도로 사용가능 
    - 디버깅 모드를 사용 할 경우 장고는 문제를 쉽게 파악하고 해결 할 수 있게 상세한 에러 메세지를 보여줌 

1. 이외
    - 간단하고 확장 할 수 있는 템플릿 텍스트 처리 엔진 (template and text filtering engine)
    - 폼을 만들고 사용자 입력을 검사하는 유효성 검사 API
    - 확장할 수 있는 인증 시스템 
    - 성능 향상에 도움이 되는 캐싱 시스템 
    - RSS 피드를 만들어주는 피드 시스템(feed framework)

---
## Django Structure
```py
Django web project
ㄴ Web01(127.0.0.1:8000/board/index)
    # 공통으로 통제하기 수월함
    # 프로젝트 설계를 위한 python 패키지들 이저장    
    ㄴ __init__.py 
    # 디렉토리를 패키지처럼 다루라고 알려주는 파일 
    # 이름이 중복되는것을 피하게 하는 모듈의 모음 
    ㄴ setting.py 
    # 프로젝트의 환경 및 구성을 저장
    #- 환경 설정이 어떻게 동작하는지 확인
    #- 데이터베이스, 사이트 언어 설정
    ㄴ urls.py
    # 현재 Django project 의 URL 선언을 저장 => 사이트의 '목차'
    # url주소와 장고의 기능을 연결 시켜주는 역활 
    # 장고의 강력한 기능**
    ㄴ manage.py
    # 프로젝트를 관리하는 스크립트 
    # admin.py와 코드를 공유 
    ㄴ Member
        ㄴ views.py (함수형 뷰)
        ㄴ urls.py  (함수형 뷰 호출 => member/views.py로부터)
        # member 
        ㄴ models.py
    ㄴ Static (CSS)
        ㄴ CSS
    ㄴ Templates(HTML)
        ㄴ member
            ㄴ index.html
    ㄴ Board(app폴더)
        ㄴ views.py 
        ㄴ urls.py  
        ㄴ models.py
```
---
## 게시판 글쓰기 만들기
- write.html
[django 서버 구동시]
```bash
    $ python manage.py runserver  $ # django 서버 구동
    $ django-admin startapp board $ #  board앱 생성
```


### url 연결
C:\Users\admin\Documents\python_basic\2py_web\django\web1\board\urls.py
- 다음내용 추가 : path('write', views.write, name='write'),

    ``` py
    from django.urls import path
    from . import views

    urlpatterns = [
        # index를 url끝에 치면 views의index함수를 불러와라
        path('write', views.write, name='write'),
    ]
    ```
   
C:\Users\admin\Documents\python_basic\2py_web\django\web1\web1\urls.py    
- 다음 내용 추가 path('board/', include('board.urls')),
    ```py
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
    ```
### 함수 정의
C:\Users\admin\Documents\python_basic\2py_web\django\web1\board\views.py
- 다음 내용 추가
```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection 

@csrf_exempt
def write(request):
    if request.method == 'GET':
        return render(request, 'board/write.html')
```
### write.html 만들기
C:\Users\admin\Documents\python_basic\2py_web\django\web1\templates\board\write.html

### 구동 확인
http://127.0.0.1:8000/board/write

### model으로 DB에 생성

```py
from django.db import models

class Table1(models.Model):
    object = models.Manager() # vs code 오류 제거용

    no      = models.AutoField(primary_key=True) 
    title   = models.CharField(max_length=200)
    content = models.TextField()
    writer  = models.CharField(max_field=50)
    hit     = models.IntegerField()
    regdate = models.DateTimeField(auto_now_add=True)
```
### 

C:\Users\admin\Documents\python_basic\2py_web\django\web1\web1\settings.py
```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board', 
]
```
### anaconda 에서 
```bash
    $ python manage.py check                # 문제없음 확인
    $ python manage.py makemigrations board # 만들기
    $ python manage.py migrate              # 이동하기
```
### web1\board\urls.py 
- 다음 추가
``` py
    path('list', views.list, name='list'),
```
### board\views.py
``` py
@csrf_exempt
def list(request):
    if request.method == 'GET':
        return render(request, 'board/list.html')
```

### templates\board\list.html
- 리스트
``` py
</title> 과 </head> 사이에 다음을 추가
<link  rel="stylesheet" href="/static/css/bootstrap.min.css" />
바디에
    <div class='container'>
        <h1>게시판 목록</h1>
        <a href='/board/write' class='btn btn-primary'>글쓰기</a>
        <table class = 'table'>
            <tr>
                <th>번호</th>
                <th>제목</th>
                <th>작성자</th>
                <th>조회수</th>
                <th>날짜</th>
            </tr>
        </table>
    </div>
```
### templates\board\write.html
- 글쓰기 페이지에 입력란 추가
<title>글쓰기</title>
    <link  rel="stylesheet" href="/static/css/bootstrap.min.css" />
</head>
<body>
    <form action='/board/write' method='post'>
    <div class="container">
        <h3>게시판 글쓰기</h3>
        <div class="form-inline" style="margin-bottom: 5px;">
            <label>글제목</label>
            <input type="text" style="width:400px" 
                name='title' class="form-control"/>
        </div>
        <div class="form-inline">
            <label>글내용</label>
            <textarea rows="6" style="width:400px"
                name='content' class="form-control"></textarea>
        </div>
        <div class="form-inline">
            <label>작성자</label>
            <input type="text" style="width:400px" 
                name='writer' class="form-control"/>
        </div>
        <div class="form-inline">
            <input type="submit" class="btn btn-primary"
                value="글쓰기"/>
            <a href="/board/list" 
                class="btn btn-secondary">목록으로</a>   
        </div>
    </div>
    </form>
</body>
</html>

### board\views.py
``` py

    elif request.method == 'POST':
        arr = [
            request.POST['title'],
            request.POST['content'],
            request.POST['writer']
        ]
        print(arr)
        return redirect('/board/list') # <a href 와 같음
```
### web1\board\templates\board\list.html

a태그는 <a href=> GET만 가능


### web1\board\templates\board\content.html
- tr, th, td 는 table row(표 셀의 가로줄), header(셀 해더), data(내용)

<body>
    <div class="container">
        <div style="margin-top:5px; margin-bottom: 5px;">
            <h3>글내용</h3>
        </div>
        <table class="table">
            <tr>
                <th class="bg-light">글번호</th>
                <td>{{ one.0 }}</td>
            </tr>
            <tr>
                <th class="bg-light">제목</th>
                <td>{{ one.1 }}</td>
            </tr>
            <tr>
                <th class="bg-light">내용</th>
                <td>
                    {% autoescape off %}
                    {{ one.2 | linebreaksbr }}
                    {% endautoescape %}
                </td>
            </tr>
            <tr>
                <th class="bg-light">작성자</th>
                <td>{{ one.3 }}</td>
            </tr>
            <tr>
                <th class="bg-light">조회수</th>
                <td>{{ one.4 }}</td>
            </tr>            
            <tr>
                <th class="bg-light">날짜</th>
                <td>{{ one.5 }}</td>
            </tr>            
        </table>
        <a href="/board/list" class="btn btn-success">목록으로</a>
        <a href="/board/content" class="btn btn-success">이전글</a>
        <a href="/board/content" class="btn btn-success">다음글</a>
        <a href="/board/edit" class="btn btn-success">글수정</a>
        <a href="/board/delete" class="btn btn-success">글삭제</a>
    </div>
</body>

### http://127.0.0.1:8000/admin/ 환경구축
- Oracle SQL Developer 와 같은 관리용 사이트
- anaconda에서 다음과 같이 입력
```
 $ conda list => django 버전확인
 $ pip install django==2.2.5 => version 변경(기존것 자동삭제)
 $ python manage.py createsuperuser
       L id/pw = admin/1234
 $ pyhton manage.py runserver
```

#### 다른사람것 참고사항
# Django WEB 


## Step01     
- Web 폴더 생성     
    - Istall Django Web     
        - Django 모듈 설치    
    - Newproject 생성     
        - 확인 할 부분 !! manage.py있는지 확인 잘 생성 되었으면    
    - 생성한 프로젝트 폴더로 이동      
    - cd C:\python_basic\2py_web\django\web1

``` py 
# Istall Django Web
$ cd C:\web_project\web01
- 설치 하고자 했던 위치로 폴더 이동     
    - 예시) 자기 폴더 위치 C에 생성하시오 => 빠르고 편함     
        - My_Path01 [C:\web_project\web01]     
        - My_Path02 [C:\web_project\web_re]     
 
# Django 모듈 설치( if 모듈이 없다면! 설치_conda OR pip whatever you want)
    $ conda install django     

# Newproject 생성(원하는 이름(whatever you want)의 폴더를 생성)
    $ django-admin startproject Newproject   

# 확인 할 부분 !! manage.py있는지 확인 잘 생성 되었으면 다음 step으로 이동 
    # 생성한 프로젝트 폴더로 이동
    $ cd Newproject 
#========================================================================
## Step 02 
- Web 요소 구성하기     
    - Board 앱 생성(여러개 생성 가능)    
    - Member 앱 생성     
    - Django 서버 구동(http://127.0.0.1:8000/)    
        - Page 열리는지 확인 => 확인 후       

```py    
# Board 앱 생성(여러개 생성 가능)
    $ django-admin startapp board

# 의문사항 => 직접해보자 
    $ django-admin.py startapp member
    $ django-adminb startproject member
# Member 앱 생성
    $ django-admin startapp member 
# Django 서버 구동(http://127.0.0.1:8000/)
    $ python manage.py runserver 

# DB 연동=> SET IT UP**
    $ python manage.py migrate
```
---
2. 기능추가
- INDEX 페이지 생성
    - URL주소와 장고의 기능을 연결하기 위해  web_re\urls.py에서 urls를 지정
    - ```web_re\urls.py```의 path()함수 안에 ```urls주소/```를 불러 올 url 정보 혹은 동작을 어디에서부터 가지고 올건지를 정의  => urls주소\urls.py    
        - ```include('urls주소\.urls') # 경로를 포함한다.  ```
        => member 폴더안에 member\urls.py를 생성하고 경로를 직접적으로 지정         
        **중요 => import include를 까먹지 말것 !!**       
    - 동작 확인을 하기 전     
        - 예를들면 member app안에 urls를 작성!       
            - view로 이동 => 동작을 만든다(메소드 생성)  
            - HTML 파일을 만든다.        
                - 만약 템플릿 폴더가 없다면 먼저 생성하고 파일을 만든다.       
        