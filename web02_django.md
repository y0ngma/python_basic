# Django WEB 
---
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
