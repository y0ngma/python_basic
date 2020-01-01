# Django WEB 
## 구조 파악
```
Django web project
    ㄴ Web01(127.0.0.1:8000/board/index)
        => 공통으로 통제하기 수월함
        ㄴ urls.py
            ㄴ 설정 파일 
                - url주소와 장고의 기능을 연결 시켜주는 역활 
        ㄴ setting.py
            ㄴ 설정 파일 
                - DB
                - 사이트 언어
    ㄴ manage.py
    ㄴ Member
        ㄴ views.py (함수형 뷰)
        ㄴ urls.py  (함수형 뷰 호출 => member/views.py로부터)
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
    ㄴ Blog 
```
---
## Step00
- 새로운 프로젝트를 만듭니다.    
- 프로젝트의 데이터베이스를 생성하고 관리합니다.     
- 프로젝트 상태를 테스트 합니다.      
- 개발용 웹 서버를 실행합니다.     
---

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
                    
        ### 의문 1. 
        ```py
        # index 
        def index(request):
        #return HttpResponse(" 열었다 ")
        return render(request,'member/index.html') 
        # <= 이건 왜 안됨? 복잡할때 사용한다는데 글쎄 
        ```
    - LOGIN 페이지 생성 
        - 위 내용반복 임으로 생략하고 진행 

    - Singin 페이지 생성 

### Django 에서는 기본적으로 CSRF 토큰을 이용해 CSRF공격을 방지
 >CSRF 공격이란?
CSRF 공격(Cross Site Request Forgery)은 웹 어플리케이션 취약점 중 하나로, 인터넷 사용자(희생자)가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 만드는 공격


<br>       

- **Sep2**    
   
   
- **Sep3**  
    - 기능을 추가 



---







---
### SQLite 설치
- 오라클 사용할거라 그냥 실습
- 설치는 아래 링크로 이동 
> 4번째_DB Browser for SQLite - .zip (no installer) for 64-bit Windows  
[주소로 이동](https://sqlitebrowser.org/dl/)

# Django DB 연동

```bash
$ cd C:\python_basic\2py_web\django\web1
$ conda install django
$ django-admin startproject project1  <= project1생성(원하는 이름의 폴더를 생성)
$ cd project1 <= 생성한 프로젝트 폴더로 이동
$ django-admin startapp member <= member 앱 생성
$ django-admin startapp board <= board 앱 생성(여러개 생성 가능)
$ python manage.py runserver <= django 서버 구동(http://127.0.0.1:8000/)

# flask -> django의 DB로
$ python manage.py migrate

```
## 4번째_ DB Browser for SQLite 
- .zip (no installer) for 64-bit Windows[주소로 이동](https://sqlitebrowser.org/dl/)
---

- Django web project
    - Web01 => 공통으로 통제하기 수월함
        - urls.py () 
        - setting.py ()
    - manage.py
    - Member
        - views.py (함수형 뷰)
        - urls.py  (함수형 뷰 호출 => member/views.py로부터)
    - Static (CSS)
        - CSS
    - Templates(HTML)
        - member
            - index.html
    - Board
    - Blog 


---
