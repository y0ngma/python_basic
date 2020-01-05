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
# 기본 구조
Django web project
    ㄴ Web01
        ㄴ __init__.py 
            - 장고는 파이썬 패키지 
            => 이름이 중복되는것을 피하게 하는 모듈의 모음 
        ㄴ setting.py 
            - 장고 프로젝트 설정 파일 
            - 데이터베이스, 사이트 언어 설정 
        ㄴ urls.py
            - 설정파일 
                - url주소와 장고의 기능을 연결 시켜주는 역활 
                - 장고의 강력한 기능**
    ㄴ manage.py
        - 프로젝트를 관리하는 스크립트 admin.py와 코드를 공유 
```

---

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
## Step 03 
- **Sep1**           
    1.  Web 구성하기           
        - Memebr : 회원 관리      
            - 로그인       
            - 회원가입     
            - 회원정보수정     
            - 로그아웃
        - Board  : 유저 인터페이스      
            - 서비스    
                - 게시판 : Q&A       

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
           