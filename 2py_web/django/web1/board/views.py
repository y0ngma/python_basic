# board/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection 

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
        
        # 조회수 1 증가 시키고 가져오자
        if request.session['hit'] == 1:
            sql = '''
                UPDATE BOARD_TABLE1 
                SET HIT = HIT+1
                WHERE NO = %s
            '''
            cursor.execute(sql, [no])
            request.session['hit'] = 0
            
        sql = '''
            SELECT
                NO, TITLE, CONTENT, WRITER, HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS')
            FROM 
                BOARD_TABLE1
            WHERE
                NO = %s
        '''
        cursor.execute(sql, [no])
        data = cursor.fetchone() # 글 번호가 일치하는것만 가져오니까 1개
        return render(request, 'board/content.html', {'one':data})

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
        arr = [
            request.POST['title'],
            request.POST['content'],
            request.POST['writer']
        ]
        print(arr)
        try :
            sql = '''
                INSERT INTO BOARD_TABLE1
                (TITLE, CONTENT, WRITER, HIT, REGDATE)
                VALUES(%s, %s, %s, 0, SYSDATE)    
            '''
            cursor.execute(sql, arr)
            print('업로드')
        except Exception as e:
            print('에러')
        return redirect('/board/list') # <a href 와 같음 
