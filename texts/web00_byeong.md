
# class_log.py

django.xmind 파일 안에 파일트리를 보면서 웹프로그래밍 환경을 구축하자

###############################<웹브라우저에 웹페이지 생성을 위한 환경구축작업>################################
1. 지정된 폴더(Private_Training)에서 django를 설치한다
    - anaconda prompt창 실행
    - conda list 입력
    - django 설치 여부 확인
    - 설치 되어 있을 경우, django의 버전을 확인한다
    - pip install django==2.2.5 입력 => 2.2.5 버전 설치한다
    - C:\Users\bcduc\Desktop\Private_Training\Private_Training 디렉토리에 django 폴더가 생성 된다

2. django 서버를 구동 시켜 본다
    - anaconda prompt창 실행
    - C:\Users\bcduc\Desktop\Private_Training\Private_Training\django\web1 디렉토리로 이동
        - cd C:\Users\bcduc\Desktop\Private_Training\Private_Training\django\web1 입력
    - manage.py를 이용해서 서버를 구동한다
        - python manage.py runserver 입력
        - 이때 python manage.py runserver 0.0.0.0:8001이라고 하면 서버를 추가로 구동할 수 있다
        - 왜 이게 가능한지에 대해서는 정확하게 이해 못했다. => 물어봐야 한다.
    - 서버 구동 후, 최초 URL을 확인한다.
    - http://127.0.0.1:8000/ 을 웹브라우저에 입력하여 접속한다 => 성공적인 설치를 확인 할 수 있다

3. 웹 프로젝트 생성
    - anaconda prompt창 실행
    - ...\django\web1 로 이동
    - django-admin startproject web1 입력 => 프로젝트 web1 생성
    - web1에 생성된 모듈들을 확인하면서 무엇이 있는지 전반적으로 파악하자

4. 웹 어플리케이션 생성
    - anaconda prompt창 실행
    - ...\django\web1 로 이동
    - django-admin startapp member 입력 => member app 생성
    - 생성된 모듈들을 확인 하면서 무엇이 있는지 전반적으로 파악하자

5. VS code 실행
    - web1\urls.py 코드 열기
    - 주석문을 확인하면 새로운 URL을 입력하기 위한 설명이 나온다
    - 설명대로 member URL을 추가 해주자
    - 이 때, 입력해서 코드를 돌려보면, 웹페이지에서 오류가 난다
    - 왜냐하면, member.urls를 불러들였는데 member.urls 파일이 아직 없기 때문이다

6. memeber/urls.py 생성하기
    - 어플리케이션을 생성 했을 때, urls.py 파일이 없다
    - 생성 시켜주고, 코드를 쓴다
    - https://docs.djangoproject.com/en/3.0/topics/http/urls/ 에 접속해서 URL namespaces에 있는 양식을 따른다
    - from django.urls import path
      from . import views

      urlpatterns = [
      path('index', views.index, name='index'),
      ]
    - 이 때, views.py에 index 함수가 없어서 오류가 나는 것을 확인 할 수 있다.

7. views.py에 index 함수 만들어 주기
    - 먼저 가장 간단하게 index를 만들어 보기 위한 패키지를 불러오자
    - from django.http import HttpResponse
      def index(request):
        return HttpResponse('index page')
    - 웹 브라우저에서 http://127.0.0.1:8000/member/index에 접속 해본다
    - 이 때, HttpResponse 함수를 이용하면 텍스트 작업이 너무 어려워 진다  => render 함수를 이용하자
    - 지금까지 작성한 함수는 주석문 처리 하고 새로 코드를 쓴다
    - render 함수를 사용하기 위해서는 외부엣 html파일을 작성해서 views.py 에서 불러 들여야 한다

8. templates 디렉토리를 만들어 준다
    - \web1\templates 디렉토리를 만들어 준다
    - render 함수에 들어갈 html 파일들을 \web1\templates 디렉토리 안에 보관해서 관리한다
    - index.html 파일을 하나 생성해서 'index page'라고 쓴다 (임의의 데이터를 입력해도 상관 없다)
    - from django.urls import path, render
      def index(request):
        return render(request,'index.html')
    - 이렇게 해서 코드를 돌리면 웹페이지에서 아무 데이터를 받지 못했다고 오류가 뜬다
    - 왜냐하면 index.html 파일을 불러 오기 위한 경로를 모르기 때문이다 => 설정해야 한다

9. web1\setting.py에서 TEMPLATES 경로 설정
    - BASE_DIR의 주석을 보면 디렉토리를 설정할 때의 방법을 알려준다
    - os.path.join(BASE_DIR,'template') 입력
    - print(os.path.join(BASE_DIR,'template')) => 디렉토리 주소가 문자열로 나옴
    - 코드를 실행하면 웹브라우저에서 정상작동한다
############################################################################################


################################<회원계정관리 웹페이지 만들기>#################################

10. 회원계졍관리를 위한 항목들 선정
    - 회의를 통해서 먼저 어떤 항목들을 생성할 것인지 논의
    - 처음부터 완벽하게 항목들을 선정하는건 사실상 불가능하다
    - 따라서, 먼저 핵심적인 기능들을 구현하기 위한 항목들을 선정 한다
    - index, list, sign_up, login

11. views.py에 함수들을 작성
    - list, sign_up, login
    - 이 때, index 함수를 제외하고는 웹 브라우저상에서 입력받은 데이터를 처리 해야 한다
    - request의 method를 고려 해야한다. (GET or POST)
    - from django.shortcuts import render
      from django.http import HttpResponse


      # def index(request):
      #     return HttpResponse('index page')

      def index(request):
          if request.method == 'GET':
              return render(request,'index.html')

      def login(request):
          if request.method == 'GET':
              return render(request,'login.html')

      def sign_up(request):
          if request.method == 'GET':
              return render(request,'sign_up.html')

      def list(request):
          if request.method == 'GET':
              return render(request,'list.html')
    - 이 때, 브라우저에서 웹페이지에 접속하면, request를 prompt창에 출력해준다.

12. templates에 위의 함수들에 대한 html파일을 생성
    - list.html, sign_up.html, login.html

13. member.py 에서 url 연동하기
    - from django.urls import path
      from . import views

      urlpatterns = [
          path('index', views.index, name='index'),
          path('login', views.login, name='login'),
          path('sign_up', views.sign_up, name='sign_up'),
          path('list', views.list, name='list'),

      ]
14. sign_up.html 작성하기
    - 회원가입에서 핵심 기능은 사용자가 입력하는 데이터를 받아서 Oracle(데이터베이스)로 보내는 것이다
    - 따라서, html작성을 통해 사용자가 데이터를 입력하도록 하고, 받은 데이터를 Oracle로 연동 하자
    - VS code에서 sign_up.html 파일을 열고 Django HTML을 html로 바꿔 준다
    - !를 눌러서 html의 가장 일반적인 양식을 로드 한다
    - <!DOCTYPE html>
          <html lang="en">
          <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <meta http-equiv="X-UA-Compatible" content="ie=edge">
              <title>sign_up</title>
          </head>
          <body>
              <h3>회원가입</h3>
                  아이디 : <input type="text" name='id'/><br/>
                  비밀번호 : <input type="password" name='pw'/><br/>
                  비밀번호 재확인 : <input type="password" name='pw'/><br/>
                  이름 : <input type="text" name='name'/><br/>
                  생년월일 : <input type="date" name='birth'/><br/>
                  성별 : <input type="text" name='sex'/><br/>
                  이메일 : <input type="email" name='email'/><br/>
                  휴대전화 : <input type="text" name='phone'/><br/>
          </body>
          </html>
    - 코드를 실행하면 웹페이지에 데이터를 입력할 수 있는 박스들이 생긴다
    - 하지만, 입력받은 데이터를 데이터 베이스로 전송해야 하는데, 아직 데이터베이스가 연동이 되어 있지 않다.
    - 또한, 데이터베이스로 데이터를 보내기 위한 송신이 준비되어 있지 않다

####################################################################################################### 

###############################<웹 어플리케이션과 Oracle(DataBase)와 연동하기>################################

15. docker 설치
    - docker 설치가 필요하다.
    - docker 툴박스 다운로드 : https://github.com/docker/toolbox/releases
    - 받은 파일을 실행시켜서 docker를 설치 한다
    - virtual box를 실행시켜서 메모리를 할당한다

16. oracle 설치
    - 이 때, 컴퓨터 사용을 깔끔하게 하기 위해서 oracle을 docker로 만든 container 안에 oracle을 설치한다
    - docker 실행
    - docker search oracle-12c 입력 후 , truevoly/oracle-12c 가 있는지 확인
    - docker pull truevoly/oracle-12c 입력해서 이미지를 가져 온다
    - docker images 입력 후, 확인
    - 컨테이너 만들기 (최초 1 회만)
        - docker run --name oracle12c -d -p 32765:8080 -p 32764:1521 truevoly/oracle-12c를 입력해준다
        - 32765와 32764는 윈도우 port 번호
        - 8080과 1521은 docker container의 port 번호
        - oracle은 8080port에 설치된다. 그리고 윈도우의 32765port와 연결된다
        - docker logs oracle12c 입력해서 설치 완료인지 확인
        - docker ps -a  => 구동중인 컨테이너 확인
    - http://ihongss.com/zip/java8.zip를 다운 받아서 
    - http://ihongss.com/zip/sqldeveloper.zip => 압축 풀어서 바탕 화면에
        - oracle 설치 시, java jdk 디렉토리 지정 해줘야 한다.
    - http://ihongss.com/zip/oracle_client.zip => 압축 풀어서 C 드라이브에 옮겨준다
    - 시스템 속성 폴더 -> 환경변수 -> 시스템변수의 path를 실행 -> instantclient_19.3 폴더를 찾아보기해서 넣어준다
    

            
17. docker container 구동 및 구동 중지
    - docker start oracle12c => 컨테이너 구동
    - docker stop oracle12c => 옵션) 컨데이너 실행 중지
    - docker rm oracle12c => 옵션) 컨테이너 삭제
    - docker ps -a  => 구동중인 컨테이너 확인

18. oracle 계정생성
    - sqldeveloper를 실행시킨다
    - 계정이 없기 떄문에 최초로 로그인 할 때는, 관리자 계정으로 접속한다
    - id: system, pw: oracle
    - 계정을 생성한다
        - oracle 명령창에 CREATE user admin IDENTIFIED BY 1234; grant connect, resource, dba to admin;를 입력한다
    - system 계정 로그아웃하고 admin 계정으로 로그인 한다
    - oracle 설치 완료

19. 웹 어플리케이션과 Oracle(Data Base)연동
    - vs code를 실행 시켜서 web1/setting.py를 연다
    - DATABASES 항목을 완성 시킨다
        - DATABASES = {
            'default' : {
                # oracle
                'ENGINE': 'django.db.backends.oracle',
                'NAME': 'xe', #SID
                'USER': 'admin',
                'PASSWORD' : '1234',
                'HOST' : '192.168.99.100',
                'PORT' : '32764'    
            }
        }
    - sqlite DB사용시
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

    - mysql 사용시
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB명',
        'USER': '아이디명',
        'PASSWORD' : '암호',
        'HOST' : '127.0.0.1',
        'PORT' : '포토번호'
20. django에서 기본적으로 제공하는 데이터 테이블들 오라클로 전송
    - anconda prompt창에서 manage.py가 있는 디렉토리로 이동
    - python manage.py migrate 입력해서 오라클에서 새로고침 하기
    - 필요한 테이블 자료들이 넘어왔는지 확인

###########################################################################################################

#####################################< 회원 계정 웹페이지 및 데이터 베이스 구축>#####################################

21. sign_up.html에 form tag 달기
    - 웹 브라우저에서 입력받은 데이터를 데이터베이스로 보내기 위해서는 form tag와 submit 기능이 필요하다
    - <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>sign_up</title>
      </head>
      <body>
          <h3>회원가입</h3>
              <form action="/member/sign_up" method="POST">
                  아이디 : <input type="text" name='id'/><br/>
                  비밀번호 : <input type="password" name='pw'/><br/>
                  비밀번호 재확인 : <input type="password" name='pw'/><br/>
                  이름 : <input type="text" name='name'/><br/>
                  생년월일 : <input type="date" name='birth'/><br/>
                  성별 : <input type="text" name='sex'/><br/>
                  이메일 : <input type="email" name='email'/><br/>
                  휴대전화 : <input type="text" name='phone'/><br/>
                  <input type="submit" value="sign_up"/>
              </form>
      </body>
      </html>
      - 위의 코드를 입력하고 웹페이지 상에서 sign_up 버튼을 누르면 CSRF validation 오류가 뜬다
      - 사이트 간 요청 위조(또는 크로스 사이트 요청 위조, 영어: Cross-site request forgery, CSRF, XSRF)는 웹사이트 취약점 공격의 하나로,
        사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 하는 공격을 말한다.
        유명 경매 사이트인 옥션에서 발생한 개인정보 유출 사건에서 사용된 공격 방식 중 하나다.
        사이트 간 스크립팅(XSS)을 이용한 공격이 사용자가 특정 웹사이트를 신용하는 점을 노린 것이라면,
        사이트간 요청 위조는 특정 웹사이트가 사용자의 웹 브라우저를 신용하는 상태를 노린 것이다. 일단 사용자가 웹사이트에 로그인한 상태에서 사이트간 요청 위조 공격 코드가 삽입된 페이지를 열면, 공격 대상이 되는 웹사이트는 위조된 공격 명령이 믿을 수 있는 사용자로부터 발송된 것으로 판단하게 되어 공격에 노출된다.
      - django 서버에서 csrf package를 가져와서 views의 함수들에 적용 해야 한다datetime A combination of a date and a time. Attributes: ()

22. csrf validation
    - @csrf_exempt
      def sign_up(request):
      if request.method == 'GET':
          return render(request,'sign_up.html')
    - 이렇게 작성하면 views.py 가 실행 될때, 함수가 csrf validation error를 일으키지 않는다.
    - 여기서 코드를 실행시키면 HttpResponse object가 없다고 에러가 난다
    - 데이터 베이스가 연동은 되었지만 데이터 베이스를 받을 그릇이 준비되어 있지 않다

23. 데이터 베이스에 테이블 만들기
    - 두가지의 방법이 있다
        - models.py를 이용하는 방법
        - oracle에서 직접 만드는 방법
    - 여기서는 먼저 oracle에서 직접 테이블을 만들자
    - oracle에서 접속하여 새 테이블을 작성한다
    - colunm의 수는 변수의 수 보다 하나 더 많이 만들어서 JOINDATE를 입력하자
    - 데이터의 형을 상황에 맞게 잘 설정하자

24. views.py의 sign_up 함수 수정 및 추가하기
    - 먼저 데이터베이스에 sql문을 실행시킬 수 있도록 cursor가 필요하다
    - from django.db import connection을 입력한다
    - cursor = connection.cursor()를 함수 바깥에서 입력해서 다른 함수에서도 쓸 수 있게 코드블럭을 구성한다
    - 추가로 회원가입 버튼을 누르고 데이터가 성공적으로 전송되면 index 창으로 돌아가도록 해야 한다
    - redirect 함수도 추가로 가져 온다
    - from django.shortcuts import render, redirect 입력
    - @csrf_exempt
    - def sign_up(request):
          if request.method == 'GET':
              return render(request,'sign_up.html')
          if request.method == 'POST':
              id = request.POST['id']
              ar = [id]
          sql = '''
              INSERT INTO MEMBER(ID, JOINDATE)
              VALUES (%s, SYSDATE)
          '''
          cursor.execute(sql,ar)
          return redirect('/member/index')
    - 코드를 실행시키면 오라클에 데이터가 저장되는걸 확인 할 수 있다

25. sign_up 함수 코드 완성 및 sign_up html 코드 완성하기
    - <view.sign_up>
    - @csrf_exempt
    - def sign_up(request):
          if request.method == 'GET':
              return render(request,'sign_up.html')
          if request.method == 'POST':
              id = request.POST['id']
              pw = request.POST['pw']
              name = request.POST['name']
              birth = request.POST['birth']
              sex = request.POST['sex']
              email = request.POST['email']
              phone = request.POST['phone']
            
              ar = [id, pw, name, birth, sex, email, phone]
              print(ar)
          sql = '''
              INSERT INTO MEMBER(ID, PW, NAME, BIRTH, SEX, EMAIL, PHONE, JOINDATE)
              VALUES (%s, %s, %s, %s, %s, %s, %s, SYSDATE)
          '''
          cursor.execute(sql,ar)
          return redirect('/member/index')
    - html 파일은 Naver에서 스타일을 코드를 그대로 배껴오자
    - 이 떄, 웹페이지 스타일을 배끼기 위해서 static 디렉토리를 만들어주고 setting.py에 연동해주자
    - STATIC_URL 아래에 STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]라고 입력해주자
    - 그리고 원하는 css 파일은 static/css 디렉토리에 저장해준다
    - 기본적으로 open source로 제공하는 bootstrap을 받아보자
    - https://getbootstrap.com/docs/4.4/getting-started/download/에 접속해서 다운로드 한다
    - 압축풀고 css파일만 static/css 디렉토리에 저장


    


