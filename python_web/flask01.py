

# 127.0.0.1 IP주소를 naver.com으로 도메인을 사서 연결
# 접속시 포트번호 80번을 쳐서 서버로 들어옴
# 사용자는 html 코드를 받아오고 크롬이 링크된 광고 등으로 바꿔줌
# 127.0.0.1:5000 => naver.com:80 
# 127.0.0.1/join => naver.com/join

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=['GET']) 
def index():
    return render_template('index.html') 

@app.route("/join", methods=['GET']) 
def join():
    #return "join page <hr/><hr     />*5" # 줄넣어 꾸미기
    return render_template('join.html') 
    # 코드여러줄을 html화면으로 렌더링하라

@app.route("/join", methods=['POST'])
def join_post():
    # DB에 값을 넣고
    print("join-post")
    return redirect("/login")  #
        # 127.0.0.1:5000/을 크롬에서 엔터친것 처럼 동작 
        # "/congrat" 가입축하페이지 등으로 가도 됨

@app.route("/login", methods=['GET']) 
def login():
    return render_template('login.html') 
    
@app.route("/login", methods=['POST']) 
def login_post():
    print("login-post")
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True) # 
        # 코드 추가시 서버다시 껐다가 켤 필요없게 바로 적용 개발모드
        # app.run(안에 debug=True추가해준다.)

