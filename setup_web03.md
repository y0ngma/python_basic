## 게시판 글쓰기 만들기
- write.html
[django 서버 구동시]
```
    $ python manage.py runserver  $ => django 서버 구동
    $ django-admin startapp board $ =>  board앱 생성
```


### url 연결
C:\Users\admin\Documents\python_basic\2py_web\django\web1\board\urls.py
- 다음내용 추가 : path('write', views.write, name='write'),

    ``` 
    from django.urls import path
    from . import views

    urlpatterns = [
        # index를 url끝에 치면 views의index함수를 불러와라
        path('write', views.write, name='write'),
    ]
    ```
   
C:\Users\admin\Documents\python_basic\2py_web\django\web1\web1\urls.py    
- 다음 내용 추가 path('board/', include('board.urls')),
    ```
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
```
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

```
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
```
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
```
    $ python manage.py check                # 문제없음 확인
    $ python manage.py makemigrations board # 만들기
    $ python manage.py migrate              # 이동하기
```
### web1\board\urls.py 
- 다음 추가
    path('list', views.list, name='list'),

### board\views.py
        
@csrf_exempt
def list(request):
    if request.method == 'GET':
        return render(request, 'board/list.html')


### templates\board\list.html
- 리스트
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

    elif request.method == 'POST':
        arr = [
            request.POST['title'],
            request.POST['content'],
            request.POST['writer']
        ]
        print(arr)
        return redirect('/board/list') # <a href 와 같음

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
 $ conda list => django version check
 $ pip install django==2.2.5 => version change(기존것 자동삭제)
 $ python manage.py createsuperuser
       L id/pw = admin/1234
 $ pyhton manage.py runserver
```
