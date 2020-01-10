### Restful
- open API
    https://www.data.go.kr/
- 실시간
    - JSON
    - Xml
- 비실시간
    - CSV 

```bash
$ pip install djangorestframework
$ django-admin start app # 
생성된 web1\api로 가서
urls.py 만듬

# web1\urls.py에서 상위 url 잡아주기 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('board/', include('board.urls')),
    path('api/', include('api.urls')),


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
    'api',
]
웹
    view
    templates 웹페이지 스마트폰(물리적으로 떨어져있음)
    
    <xml> 
    <id> achilles <id>
    <age>3</age>
    </xml>
    에서 간소화
    json
    {'id':'achilles', 'age':3}
    obj로 가져온것을 이렇게 변환해주는것이 library, pickle, serializer
    
```