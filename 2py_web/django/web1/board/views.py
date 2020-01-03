# board/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection 
from base64 import b64encode
import pandas as pd
# 동영상 등의 파일은 BLOB로 저장되는데 이 byte 배열을 base64로 변경함.
cursor = connection.cursor() # sql문 수행위한 cursor객체

# 127.0.0.1:8000/board/content?no=21
# 127.0.0.1:8000/board/content     => 오류발생
# no = request.GET['no'] # 없을때 기본값 0 을 대신 주는 함수 get


@csrf_exempt
def dataframe(request):
    if request.method == 'GET':
        df = pd.read_sql(
            '''
            SELECT NO, WRITER, HIT, REGDATE
            FROM BOARD_TABLE1
            ''', con=connection)
        print(df.columns)
        print(df)
        print(df['NO'], df['WRITER'])
        print(type(df))
        return render(request, 'board/dataframe.html', 
            {'dataframe':df.to_html(classes='table')})

    # elif request.method == 'POST':
    #     no = request.POST['no']
    #     ti = request.POST['title']
    #     co = request.POST['content']
    #     arr = [ti, co, no]
    #     sql = '''
    #         UPDATE BOARD_TABLE1
    #         SET TITLE=%s, CONTENT=%s
    #         WHERE NO=%s
    #     '''
    #     cursor.execute(sql, arr)
    #     return redirect('/board/content?no=' +  no)

@csrf_exempt
def edit(request):
    if request.method == 'GET':
        no = request.GET.get('no', 0)
        sql = '''
            SELECT NO, TITLE, CONTENT
            FROM BOARD_TABLE1
            WHERE NO = %s
        '''
        cursor.execute(sql, [no])
        data = cursor.fetchone()
        return render(request, 'board/edit.html',
            {'one':data})

    elif request.method == 'POST':
        no = request.POST['no']
        ti = request.POST['title']
        co = request.POST['content']
        arr = [ti, co, no]
        sql = '''
            UPDATE BOARD_TABLE1
            SET TITLE=%s, CONTENT=%s
            WHERE NO=%s
        '''
        cursor.execute(sql, arr)
        return redirect('/board/content?no=' +  no)

@csrf_exempt
def delete(request):
    if request.method == 'GET':
        no = request.GET.get('no', 0)
        sql = '''
            DELETE FROM BOARD_TABLE1
            WHERE NO = %s
        '''
        cursor.execute(sql, [no])
        return redirect('/board/list')

@csrf_exempt
def content(request):
    if request.method == 'GET':
        no = request.GET.get('no', 0)
        print(type(no), no)
        if no == 0:
            return redirect('/board/list') # <a href 와 같음 
    # 세션을 이용, 새로고침에 의한 조회수 증가 방지법  
        # list함수로 부터 
        if request.session['hit'] == 1:
            sql = '''
                UPDATE BOARD_TABLE1 
                SET HIT = HIT+1
                WHERE NO = %s
            '''
            cursor.execute(sql, [no])
            request.session['hit'] = 0 # # 글 번호가 일치하는것만 가져오니까 1개
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
        # 첫글/마지막글의 번호 가져오기
        sql = '''
            SELECT MAX(NO)
            FROM BOARD_TABLE1
        '''
        cursor.execute(sql)
        last = cursor.fetchone() 
        sql = '''
            SELECT MIN(NO)
            FROM BOARD_TABLE1
        '''
        cursor.execute(sql)
        first = cursor.fetchone() 
    # 내용 가져오기
        sql = '''
            SELECT
                NO, TITLE, CONTENT, WRITER, HIT, 
                TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS'), IMG
            FROM 
                BOARD_TABLE1
            WHERE
                NO = %s
        '''
        cursor.execute(sql, [no])
        data = cursor.fetchone()  #(89,)
        print('가져온 데이터는 =>', data)
        
        if data[6] : # BLOB형식으로 DB에 첨부된 사진등이있을때
            img = data[6].read() # byte배열을 img에 넣음
            img64 = b64encode(img).decode('utf-8')
        else : # 없을때 '사진없음' 이라는 이미지를 표시
            file=open('./static/img/default.jpg', 'rb')
            img = file.read()
            img64 = b64encode(img).decode('utf-8')
        print('data:{} img64:{}\n last:{}{}\n last[0]:{}{}\n str(last):{} '\
            .format(type(data),type(img64),last,type(last),last[0],type(last[0]),str(last[0])))
        return render(request, 'board/content.html', 
            {'one':data, 'image':img64, 'prv':prv[0], 
            'nxt':nxt[0], 'first':str(first[0]), 'last':str(last[0])    }   )

@csrf_exempt
def list(request):
    if request.method == 'GET':
        request.session['hit'] = 1
        sql = '''
            SELECT
                NO, TITLE, WRITER, HIT, 
                TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS')
            FROM BOARD_TABLE1 ORDER BY NO DESC 
        ''' # 글 번호 내림차순으로 descendant
        cursor.execute(sql)
        data = cursor.fetchall()
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
