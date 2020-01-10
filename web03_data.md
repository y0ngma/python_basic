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



```