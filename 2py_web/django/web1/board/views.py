# board/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection 
from base64 import b64encode
# 동영상 등의 파일은 BLOB로 저장되는데 이 byte 배열을 base64로 변경함.
cursor = connection.cursor() # sql문 수행위한 cursor객체

# 127.0.0.1:8000/board/content?no=21
# 127.0.0.1:8000/board/content     => 오류발생
# no = request.GET['no'] # 없을때 기본값 0 을 대신 주는 함수 get

@csrf_exempt
def content(request):
    if request.method == 'GET':
        no = request.GET.get('no', 0)
        print(no)
        if no == 0:
            return redirect('/board/list') # <a href 와 같음 
        
    # 조회수 1 증가값 세션에 넘겨주자
        if request.session['hit'] == 1:
            sql = '''
                UPDATE BOARD_TABLE1 
                SET HIT = HIT+1
                WHERE NO = %s
            '''
            cursor.execute(sql, [no])
            request.session['hit'] = 0

    # 이전글/다음글 
        # NVL이용 없을때 디폴트값 0 주기
        sql = '''
            SELECT NVL(MAX(NO), 0) 
            FROM BOARD_TABLE1
            WHERE NO < %s
        '''
        cursor.execute(sql, [no])
        prv = cursor.fetchone() 
        sql = '''
            SELECT NVL(MIN(NO), 0) 
            FROM BOARD_TABLE1
            WHERE NO > %s
        '''
        cursor.execute(sql, [no])
        nxt = cursor.fetchone() 

    # 내용 가져오기
        sql = '''
            SELECT
                NO, TITLE, CONTENT, WRITER, HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS'), IMG
            FROM 
                BOARD_TABLE1
            WHERE
                NO = %s
        '''
        cursor.execute(sql, [no])
        data = cursor.fetchone() # 글 번호가 일치하는것만 가져오니까 1개
        print('가져온 데이터는 =>', data)
        
        if data[6] : # BLOB형식으로 DB에 첨부된 사진등이있을때
            img = data[6].read() # byte배열을 img에 넣음
            img64 = b64encode(img).decode('utf-8')
        else : # 없을때 '사진없음' 이라는 이미지를 표시
            file=open('./static/img/default.jpg', 'rb')
            img = file.read()
            img64 = b64encode(img).decode('utf-8')

        return render(request, 'board/content.html', 
            {'one':data, 'image':img64, 'prv':prv[0], 'nxt':nxt[0]})

@csrf_exempt
def list(request):
    if request.method == 'GET':
        request.session['hit'] = 1

        sql = '''
            SELECT
                NO, TITLE, WRITER, HIT, 
                TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS')
            FROM 
                BOARD_TABLE1
            ORDER BY NO DESC 
        '''
        # 글 번호 내림차순으로 descendant
        cursor.execute(sql)
        data = cursor.fetchall()
        print(type(data)) 
        print(data) # [(    ), (    )]
        return render(request, 'board/list.html', {'abc':data})

@csrf_exempt
def write(request):
    if request.method == 'GET':
        return render(request, 'board/write.html')
    elif request.method == 'POST':
        tmp = None
        if 'img' in request.FILES:
            img = request.FILES['img'] # name값 img
            tmp = img.read()
        # img = request.FILES.get('img', None)
        arr = [
            request.POST['title'],
            request.POST['content'],
            request.POST['writer'],
            tmp # 이미지를 byte[]으로 변경
        ]
        print(arr)
        try :
            sql = '''
                INSERT INTO BOARD_TABLE1
                (TITLE, CONTENT, WRITER, IMG, HIT, REGDATE)
                VALUES(%s, %s, %s, %s, 0, SYSDATE)    
            '''
            cursor.execute(sql, arr)
            print('업로드')
        except Exception as e:
            print('에러')
        return redirect('/board/list') # <a href 와 같음 
