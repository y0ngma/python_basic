## 서버 구동방법
    # ``` $ python manage.py migrate```
    # ``` $ python manage.py runserver```
    # 끄는방법은 다음과 같다.
    # ``` $ docker stop oracle12c
    # ``` $ docker-machine stop```
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection 

cursor = connection.cursor()  
    # 모델거치지 않고 sql-DB 바로 연결시 connection필요
    # cursor 사용
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth1
from django.contrib.auth import login as login1
from django.contrib.auth import logout as logout1
    # django에서 제공하는 User 사용

####실습 시작######################################
from .models import Table2 # models.py파일의 Table2클래스
from django.db.models import Sum, Max, Min, Count, Avg

def exam_select(request):
    if request.method == 'GET':
        txt  = request.GET.get('txt', '')
        page = int(request.GET.get('page', 1))
            # 1 -> 0, 10 게시물
            # 2 -> 11, 20
        if txt=='':
            list = Table2.objects.all() [page*10-10:page*10]
                # SELECT*FROM MEMBER_TABLE2
            cnt  = Table2.objects.all().count() 
                # SELECT COUNT(*) FROM MEMBER_TABLE2
            tot = (cnt-1)//10+1
        else: 
            list = Table2.objects.filter(name__contains=txt)[page*10-10:page*10]
                # SELECT*FROM MEMBER_TABLE2 WHERE name LIKE '%가%'
            cnt  = Table2.objects.filter(name__contains=txt).count()
                # SELECT COUNT(*)FROM MEMBER_TABLE2 WHERE name LIKE '%가%'
            tot = (cnt-1)//10+1
        return render(request, 'member/exam_select.html', \
            {'list':list, 'pages':range(1,tot+1,1),'page_html':page}) # 파라미터 괄호하나에만
        # 반별 국어, 영어, 수학 합계
            # list = Table2.objects.aggregate(Sum('math'))
            #     # SELECT SUM(math) FROM MEMBER_TABLE2
            #     # WHERE CLASS_ROOM=101    
            # list = Table2.objects.all().values(['no', 'name'])
            #     # SELECT NO, NAME FROM MEMBER_TABLE2
            # list = Table2.objects.all().order_by('name')
            #     # 복잡한 SELECT은 다음과 같이 raw 안에 SQL문을 넣어 구현
            # list = Table2.objects.raw("SELECT*FROM MEMBER_TABLE2 ORDER BY name ASC") 
            # list = Table2.objects.values('classroom').annotate(kor=Sum('kor'), eng=Sum('eng'), math=Sum('math'))   
            #     # SELECT 
            #     #     SUM(kor)  AS kor, 
            #     #     SUM(eng)  AS eng, 
            #     #     SUM(math) AS math 
            #     # FROM MEMBER_TABLE2
            # return render(request, 'member/exam_select.html',{"list":list}) 

def exam_insert(request):
    if request.method == 'GET':
        # range(5) = 다섯줄씩 입력하기
        # 성씨묶음 = []5개, 국영수_점수묶음=[]3x5을 서로 묶어보기
        # 그것을 range()대신 사용해보기

        return render(request, \
        'member/exam_insert.html', {'cnt':range(10)})
            
    elif request.method=='POST':
        no  = request.POST.getlist('no[]')
        na  = request.POST.getlist('name[]')
        ko  = request.POST.getlist('kor[]')
        en  = request.POST.getlist('eng[]')
        ma  = request.POST.getlist('math[]')
        cl  = request.POST.getlist('classroom[]')
        
        objs= []
        print(na)
        print('길이:', len(na))
        print('길이:', len(ko))
        print('길이:', len(objs)) 
        for i in range(0, len(na), 1):
            obj = Table2()
            obj.name        = na[i]
            obj.kor         = ko[i]
            obj.eng         = en[i]
            obj.math        = ma[i]
            obj.classroom   = cl[i]
            objs.append(obj)
        Table2.objects.bulk_create(objs)
        return redirect('/member/exam_select')

def exam_update(request):
    if request.method == 'GET':
        n   = request.session['no']
        #n   = request.POST.get('no') #한개 
        rows = Table2.objects.filter(no__in=n)
        return render(request, 'member/exam_update.html', {'list':rows})
    elif request.method == 'POST':
        menu = request.POST['menu']
        if menu == "list":
            no = request.POST.getlist('chk[]')
            request.session['no'] = no
            return redirect('/member/exam_update')
        elif menu == "update":
            print("=================================================")
            no        = request.POST.getlist('no[]')
            name      = request.POST.getlist('name[]')
            kor       = request.POST.getlist('kor[]')
            eng       = request.POST.getlist('eng[]')
            math      = request.POST.getlist('math[]')
            classroom = request.POST.getlist('classroom[]')

            objs=[]
            for i in range(0, len(no), 1):
                obj           = Table2.objects.get(no=no[i])
                obj.name      = name[i]
                obj.kor       = kor[i]
                obj.eng       = eng[i]
                obj.math      = math[i]
                obj.classroom = classroom[i]
                objs.append(obj)
            Table2.objects.bulk_update(objs, ['name', 'kor', 'eng', 'math', 'classroom'])
            return redirect('/member/exam_select')
        else:
            return redirect('/board/list') # 엉뚱한곳으로 보내서 뭐가 잘못되었는지 파악가능

def exam_delete(request):
    if request.method == 'GET':
        n   = request.GET.get('no', 0) 
        p   = request.GET.get('page', 1) 
        row = Table2.objects.get(no=n)
        row.delete()
        return redirect('/member/exam_select?page='+p)

####실습 끝####################################
def auth_pw(request): 
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('/member/auth_login')

        return render(request, 'member/auth_pw.html')

    elif request.method == "POST": 
        pw = request.POST['pw']
        pw1 = request.POST['pw1']

        obj = auth1(request, username=request.user, password=pw)
        if obj:
            obj.set_password(pw1)
            obj.save()
            return redirect('/member/auth_index')
        return redirect('/member/auth_pw')

def auth_edit(request): 
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('/member/auth_login')
            
        obj = User.objects.get(username=request.user)

        return render(request, 'member/auth_edit.html', {'obj':obj})

    if request.method == "POST":         
        id = request.POST['username']
        na = request.POST['first_name']
        em = request.POST['email']

        obj = User.objects.get(username=id)
        obj.first_name = na
        obj.email = em
        obj.save()
        return redirect('/member/auth_index')

def auth_login(request):
    if request.method =="GET":
        return render(request, 'member/auth_login.html')
    elif request.method =='POST':
        id = request.POST['username']
        pw = request.POST['password']
        # DB에 인증
        obj = auth1(request, username=id, password=pw)
        if obj is not None:
            login1(request, obj) # 세션에 추가    
            return redirect('/member/auth_index')
        return redirect('/member/auth_login')

def auth_logout(request): 
    if request.method == 'GET' or request.method == "POST": 
            # GET으로도 로그아웃=주소창에 누군가 치면 싫어도 로그아웃된다.
        logout1(request) # 세션 초기화
        return redirect('/member/auth_index')

@csrf_exempt
def auth_index(request):
    if request.method =="GET":
        return render(request, 'member/auth_index.html')

@csrf_exempt
def auth_join(request):
    if request.method == 'GET':
        return render(request, 'member/auth_join.html')
    elif request.method =='POST':
        id = request.POST['username']
        pw = request.POST['password']
        na = request.POST['first_name']
        em = request.POST['email']
        
        obj = User.objects.create_user(
            username=id,
            password=pw,
            first_name=na,
            email=em )
        obj.save()
            # 회원가입
                # import
                # obj = Table2(
                #     email=em
                #     username=id
                # )
                #  
                # obj = Table2() 위와 동일 결과
                # obj.username=request.POST['name']
                # obj.email=em
                #
                # obj.save()

        return redirect('/member/auth_index')

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
    print(data)
        # [(, , , ,column렬의 수 만큼 ), (row 행의 수 만큼)]
        # list.html으로 넘어갈때
        # list 변수에 data값을, title변수에 회원목록 문자로 해서 넘긴다.
        # 단 title키의 값은 하나뿐이라 list.html에서 {{title}}가능하고
        # list키의 값은 회원수만큼이므로 for문 사용했음
    sql = 'SELECT*FROM MEMBER1 ORDER BY ID ASC' # vip맴버리스트 취합
    cursor.execute(sql)
    data2 = cursor.fetchall()
    print(type(data)) # 리스트
    print(data) 
    return render(request, 'member/list.html', {'list':data, 'list2':data2, 'title':'회원목록'})

def member(request):
    request.method == 'GET'
    return redirect('/member/list')

def index(request):
    request.method == 'GET'
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
    # sql용
        # sql ='''
        #     INSERT INTO MEMBER(ID,NAME,AGE,PW,JOINDATE)
        #     VALUES (%s, %s, %s, %s, date('now'))
        #     '''   
    # oracle용
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

        ar = [id, pw, na, em, te, im]
        sql = '''
            INSERT INTO MEMBER1(ID, PW, NAME, EMAIL, TEL, IMG, JOINDATE)
            VALUES (%s, %s, %s, %s, %s, %s, SYSDATE)
            '''
        cursor.execute(sql, ar)
        return redirect('/member/member')

@csrf_exempt
def edit(request):
    if request.method == "GET":
        ar = [request.session['userid']]
        sql = '''
        SELECT * 
        FROM MEMBER 
        WHERE ID=%s 
        '''
            # WHERE 는 if 문(ID는 내가 넘겨주는값이 스트링으로 동일할때)
        cursor.execute(sql, ar)
        data=cursor.fetchone()
        print(data)

        return render(request, 'member/edit.html', {'one':data})
    elif request.method == 'POST':
        ar = [
            request.POST['name'],
            request.POST['age'],
            request.POST['id']
        ]

        sql = '''
            UPDATE MEMBER SET NAME=%s, AGE=%s
            WHERE ID = %s
        '''
        cursor.execute(sql, ar)

        return redirect('/member/index')

@csrf_exempt
def login(request):
    if request.method == 'GET':
        print('loginGET')
        return render(request, 'member/login.html')
    elif request.method == 'POST':
        print('loginPOST')
        ar = [request.POST['id'], request.POST['pw']]
        sql = '''
        SELECT ID, NAME
        FROM MEMBER
        WHERE ID=%s AND PW=%s
        '''
            # *은 모두 가져오기. 가져올 때 순서대로
            # SELECT*FROM MEMBER WHERE ID=%s AND PW=%s
        cursor.execute(sql, ar)
        data = cursor.fetchone()
        print(type(data))
        print(data)

        if data:
            request.session['userid']   =data[0]
            request.session['username'] =data[1]
            for key, value in request.session.items():
                print('키값은{} 이고 밸류는{}이다'.format(key, value))
            return redirect('/member/index')
            # 세션. 
            # 암호는 가져오면 보안에 취약.
        print('로그인실패')
        return redirect('/member/index')
        
@csrf_exempt
def logout(request):
    if request.method == 'GET' or request.method== 'POST':
        del request.session['userid']
        del request.session['username']
        return redirect('/member/index')

@csrf_exempt
def delete(request):
    if request.method == 'GET'or request.method== 'POST':
        ar = [request.session['userid']]
        sql = 'DELETE FROM MEMBER WHERE ID=%s'
        cursor.execute(sql, ar)
        return redirect('/member/logout')

###################
def js_index(request):
    if request.method=="GET":
        return render(request, 'member/js_index.html')

def js_chart(request):
    if request.method=="GET":
        return render(request, 'member/js_chart.html')