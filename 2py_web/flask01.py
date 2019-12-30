

# 127.0.0.1 IP주소를 naver.com으로 도메인을 사서 연결
# 접속시 포트번호 80번을 쳐서 서버로 들어옴
# 사용자는 html 코드를 받아오고 크롬이 링크된 광고 등으로 바꿔줌
# 127.0.0.1:5000 => naver.com:80 
# 127.0.0.1/join => naver.com/join

from flask import Flask, render_template, request, redirect
import cx_Oracle as oci  #
    # pip install cx_oracle
    # (base)C:\Users\admin ```$pip install cx_oracle```
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8') #
    # 아이디/암호@서버주소:포트번호/SID
print(conn)
cursor = conn.cursor()

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template('index.html') 

@app.route('/member', methods=['GET'])
def member():
    sql = 'SELECT * FROM MEMBER'
    cursor.execute(sql)
    data = cursor.fetchall() 
    print(type(data))
    sum = 0
    mean = 0
    for i in data:
        sum += i[3]
        tmp = data.index(i)+1
        mean = sum/len(data)
        print('%d번째 회원이름:%s 무게:%d', % (tmp, i[2], i[3]))
        print('{}번째 회원의 이름:{} 무게:{}' .format(tmp, i[2], i[3]))      
    print('회원들의 평균나이는 %.1f 이다.' % mean)
    return render_template('member.html', member=mean) 

@app.route("/join", methods=['GET']) 
def join():
    print('join-get')
        #return "join page <hr/><hr     />*5" # 줄넣어 꾸미기
    return render_template('join.html') 
        # 코드여러줄을 html화면으로 렌더링하라
@app.route("/join", methods=['POST'])
def join_post():
    a = request.form['id']
    b = request.form['pw']
    c = request.form['name']
    d = request.form['age']
    sql = 'INSERT INTO MEMBER VALUES(:id, :pw, :na, :ag, SYSDATE)'
    cursor.execute(sql, id=a, pw=b, na=c, ag=d)
    conn.commit()
    print('{}:{}:{}:{}'.format(a,b,c,d))
    return redirect("/member")  
        # 127.0.0.1:5000/을 크롬에서 엔터친것 처럼 동작 
    # 오라클 DB접속하는법
    # 추가하는 SQL문 작성 => INSERT, SELECT, UPDATE, DELETE
    # SQL문 수행

@app.route("/login", methods=['GET']) 
def login():
    print('login-get')
    return render_template('login.html')
@app.route("/login", methods=['POST']) 
def login_post():
    print("login-post")
    return redirect("/member")

if __name__=='__main__':
    app.run(debug=True) # 
        # 코드 추가시 서버다시 껐다가 켤 필요없게 바로 적용 개발모드
        # app.run(안에 debug=True추가해준다.)

