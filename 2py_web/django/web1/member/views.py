## 서버 구동방법
    # ``` $ python manage.py migrate```
    # ``` $ python manage.py runserver```
    # 끄는방법은 다음과 같다.
    # ``` $ docker stop oracle12c
    # ``` $ docker-machine stop```
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection # 
    # 모델거치지 않고 sql-DB 바로 연결시 connection필요
    # cursor 사용
cursor = connection.cursor() 

def list(request): 
    # sql 쓴 이유 :
        # 데이터가 먼저냐 화면이 먼저냐?
        # GET을 쓰지 않은 이유
        # ID 기준으로 오름차순으로 가져오자
    sql = 'SELECT*FROM MEMBER ORDER BY ID ASC'
    cursor.execute(sql) # 
        # cursor는 sql 실행하기위한 단위
        # connection.execute를 사용해도 되지만 아직 세부단위 설정되지 않음
    data = cursor.fetchall() # sql문 실행의 결과값 가져와라
    print(type(data)) # 리스트
    print(data) # 
        # [(, , , ,column렬의 수 만큼 ), (row 행의 수 만큼)]
        # list.html으로 넘어갈때
        # list 변수에 data값을, title변수에 회원목록 문자로 해서 넘긴다.
        # 단 title키의 값은 하나뿐이라 list.html에서 {{title}}가능하고
        # list키의 값은 회원수만큼이므로 for문 사용했음
    return render(request, 'member/list.html', {'list':data, 'title':'회원목록'})

def member(request):
    request.method == 'GET'
    return redirect('/member/list')

def index(request):
    request.method == 'GET'
    print('indexGET')
    return render(request, 'member/index.html')
        #return HttpResponse('index page <hr />') 처럼 하던 불편사항 개선

# django에서는 보안상 csrf가 POST 할때 필수사용됨
@csrf_exempt # POST로 값을 전달 받는곳은 필수
def join(request):
    if request.method == 'GET':
        return render(request, 'member/join.html')
    elif request.method == 'POST':
        id = request.POST['id']
        na = request.POST['name']
        pw = request.POST['pw']
        ag = request.POST['age']

        ar = [id, na, ag, pw] # list로 만듬
        # for i in ar:
        #     tmp = ar[i]
        #     print('{}는 {} 이다'. format(tmp, ar))       
    # # sql용
        # sql ='''
        #     INSERT INTO MEMBER(ID,NAME,AGE,PW,JOINDATE)
        #     VALUES (%s, %s, %s, %s, date('now'))
        #     '''   
    # # oracle용
        sql ='''
            INSERT INTO MEMBER(ID,NAME,AGE,PW,JOINDATE)
            VALUES (%s, %s, %s, %s, SYSDATE)
            '''
        cursor.execute(sql, ar) # 위 sql 에 ar리스트를 순서대로 넣어라.그래서 서로 동일순. 
            # 다만, 회원가입html에서 입력순이랑 ar순서 무관. 액셀이 아니기 때문에 값을 지정해줘야 찾아가게된다.
        return redirect('/member/member')
            # 크롬에서 127.0.0.1:8000/member/member 엔터키 동일

@csrf_exempt
def join1(request):
    if request.method == "GET":
        return render(request, 'member/join1.html')
    elif request.method == "POST":
        id = request.POST['id']
        na = request.POST['name']
        pw = request.POST['pw']
        im = request.POST['img']
        te = request.POST['tel']
        em = request.POST['email']

        ar = [id, na, pw, im, te, em]
        sql = '''
            INSERT INTO MEMBER(ID, PW, NAME, EMAIL, TEL, IMG, JOINDATE)
            VALUES (%s, %s, %s, %s, %s, %s, SYSDATE)
            '''
        cursor.excute(sql, ar)
        return redirect('/member/member')

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'member/login.html')
    elif request.method == 'POST':
        return redirect('/member/member')
