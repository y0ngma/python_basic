# flask 기본 구성
# 1. 모듈가져오기
from flask import Flask, render_template
# 2. 플라스크 객체 생성
app = Flask(__name__)
# 3. 라우팅
@app.route('/') # 데코레이터. 함수안의 함수
def home():
    return 'hello flask'
# 3-1. 언어감지 처리
# GET반식만 현재 되어 있는데, POST도 지원하겠다
@app.route('/LangTypeDetect')
def LangTypeDetect():
    return render_template('index.html')

# 4. 서버가동
if __name__=='__main__':
    app.run(debug=True)