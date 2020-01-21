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

1. 이 외
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

## setup
- anaconda prompt 에서
    ``` 
    $ cd C:\python_basic\2py_web\django\web1
    원하는 경로로 이동 후 다음을 입력
    ```
    ```
    # 웹 프로젝트 생성
    $ django-admin startproject web1

    # web1디렉토리에서 필요한 앱 생성
    $ django-admin startapp member
    
---


## templates에 html만들기
```bash
    $ python manage.py runserver  $ # django 서버 구동
    $ django-admin startapp board $ # board앱 생성
```
- 메인 setting의 templates 
    ```py 
    # 60 번째 줄에 templates 경로 잡아주기
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
    ```

### 게시판 글쓰기 만들기
- 상위 프로젝트의 urls.py에서 앱urls 연결
    ```py
    # C:\Users\admin\Documents\python_basic\2py_web\django\web1\web1\urls.py    
    from django.contrib import admin
    from django.urls import path, include  # ,include 추가

    urlpatterns = [
        path('admin/', admin.site.urls),
        # 다음 내용 추가
        path('member/', include('member.urls')),
        path('board/', include('board.urls')),
        #127.0.0.1:8000/board/
    ]
    ```

    - 앱 내에 urls.py 생성
        ``` py
        # C:\Users\admin\Documents\python_basic\2py_web\django\web1\board\urls.py
        from django.urls import path
        from . import views

        urlpatterns = [
            # index를 url끝에 치면 views의index함수를 불러와라
            path('write', views.write, name='write'),
        ]
        ```


### 함수 정의
- 다음 내용 추가
    ```py
    # C:\Users\admin\Documents\python_basic\2py_web\django\web1\board\views.py
    from django.shortcuts import render, redirect
    from django.http import HttpResponse
    from django.views.decorators.csrf import csrf_exempt
    from django.db import connection 

    @csrf_exempt # html의 post줄에 입력하면 생략가능 {% csrf_token %}
    def write(request):
        if request.method == 'GET':
            return render(request, 'board/write.html')
    ```

- write.html 만들기
C:\Users\admin\Documents\python_basic\2py_web\django\web1\templates\board\write.html

- 구동 확인
    `http://127.0.0.1:8000/board/write`


### CSS 꾸미기 static setup    
    ```py    
    # 상위 프로젝트의 setting 142번째 줄에 추가
    STATIC_URL = '/static/'

    # 정적파일 경로 지정하는 방법이다.
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    CORS_ORIGIN_ALLOW_ALL = True
    ```

## model으로 DB에 입력
- 원하는 앱의 models.py에서 
    ```py
    from django.db import models

    class Table1(models.Model):
        objects = models.Manager() # vs code 오류 제거용

    # 자동의 이점 : 개발자가 번호 중복 매기지 않을 수 있음
        no      = models.AutoField(primary_key=True) # 자동 번호매기기
    # 사용자로부터 받을 내용-----------------------------
        title   = models.CharField(max_length=200) 
        content = models.TextField() 
        writer  = models.CharField(max_length=50)
        img     = models.BinaryField(null=True) # 바이너리 필수
    # -------------------------------------------------
        hit     = models.IntegerField() # 조회수
        regdate = models.DateTimeField(auto_now_add=True) # 자동

    ```

- setting 에서 

    ```py
    # C:\Users\admin\Documents\python_basic\2py_web\django\web1\web1\settings.py

    # 33번째줄
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'board',
        'member',

    ]
        
    # 80번째 줄
    DATABASES = {
        'default': {
        ## sqlite DB 사용시
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        
        ## mysql
            # 'ENGINE'   : 'django.db.backends.mysql',
            # 'NAME'     : 'DB명',
            # 'PASSWORD' : '암호',
            # 'USER'     : '아이디명',
            # 'HOST'     : '127.0.0.1',
            # 'PORT'     : '포트번호'

        ## oracle
            'ENGINE'   : 'django.db.backends.oracle',
            'NAME'     : 'xe', # SID(db명)
            'PASSWORD' : '1234',
            'USER'     : 'admin',
            'HOST'     : '192.168.99.100',
            'PORT'     : '32764'
        }
    }
    ```

- DB연동 
    - setup을 마치고 연동 실행. 
    ```bash
        $ python manage.py check                # 문제없음 확인
        $ python manage.py makemigrations board # 만들기
        $ python manage.py migrate              # 이동하기
        # models.py있는 폴더/migrations/에 연동내역 확인

        # 오류시 models.py가 있는 폴더내 migrations를 지우고 sqldevelop-DJANGO_MIGRATION 테이블의 데이터중 관련내역을 지우고 재실행 
    ```
---

## 관리자 http://127.0.0.1:8000/admin/ 환경구축
- Oracle SQL Developer 와 같은 관리용 사이트
- anaconda에서 다음과 같이 입력
    ```
    $ conda list => django 버전확인
    $ pip install django==2.2.5 => version 변경(기존것 자동삭제)
    $ python manage.py createsuperuser
        L id/pw = admin/1234
    $ pyhton manage.py runserver
    ```




