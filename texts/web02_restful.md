## Restful
- open API
    https://www.data.go.kr/
- 실시간
    - JSON
    - Xml
- 비실시간
    - CSV 

### Django Restful Framework
- 설치
    ```bash
    $ pip install djangorestframework
    $ django-admin start app # 생성된 web1\api로 가서 urls.py 만듬

    # web1\urls.py에서 상위 url 잡아주기 
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('member/', include('member.urls')),
        path('board/', include('board.urls')),
        path('api/', include('api.urls')), # 추가


    ]
    web1\settings 에서 
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'board', 
        'member',
        'api', # 추가함
    ]
    ```

### 웹
- view
- templates 웹페이지 스마트폰(물리적으로 떨어져있음)

- json 이란?
    ```html
    <xml> 
    <id> achilles <id>
    <age>3</age>
    </xml>
    ```
- 형식으로 전달하던것을 json 으로 용량을 간소화 하고 데이터 손실 없게 하여 `{'id':'achilles', 'age':3}` 으로 전송한다
- obj로 가져온것을 이렇게 변환해주는것이 library, pickle, serializer

- 택스트파일 저장시 제목을 `abc.html` 와 같이 하면 확장자포함된다.
- 내용은 다음과 같다.
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>JS SELECT</title>
    </head>
    <body>
        
        <script src="http://code.jquery.com/jquery-3.4.1.min.js" 
            integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" 
            crossorigin="anonymous">
        </script>
        <script>
            $(function(){
                $.get('http://127.0.0.1:8000/api/select1?key=abc', function(data){
                    console.log(data)
                })
            })
        </script>

    </body>
    </html>
    ```
---

### Cross Origin Resource Sharing (CORS)
- 웹 페이지 상의 제한된 리소스를 최초 자원이 서비스된 도메인 밖의 다른 도메인으로부터 요청할 수 있게 허용하는 구조이다. 웹페이지는 교차 출처 이미지, 스타일시트, 스크립트, iframe, 동영상을 자유로이 임베드할 수 있다.

    ```bash

    # CORS 사용해서 밖에서 도메인을 넣었을때 이해할 수 있게해준다.
    $ pip install django-cors-headers

    파일명 : setting.py
    INSTALLED_APPS = (
        
        'corsheaders',  
    )

    MIDDLEWARE = (
        
        'corsheaders.middleware.CorsMiddleware',    
    )

    #마지막 줄에 추가
    CORS_ORIGIN_ALLOW_ALL = True
    ```