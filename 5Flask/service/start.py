# flask 기본 구성
# 1. 모듈가져오기
from flask import Flask, render_template, request
# 2. 플라스크 객체 생성
app = Flask(__name__)
# 3. 라우팅
@app.route('/') # 데코레이터. 함수안의 함수
def home():
    return 'hello flask'
# 3-1. 언어감지 처리
# GET반식만 현재 되어 있는데, POST도 지원하겠다
# 1개의 url로 여러 메소드를 지원 => restful
@app.route('/LangTypeDetect', methods=['GET', 'POST'])
def LangTypeDetect():
    if request.method == 'POST':
        # 1. 원문데이터 획득(get, post 방식으로 전달된 데이터 획득)
        # index기법 form['ori1'] 사용하면 오류발생시 서버오류 500(INTERNAL SERVER ERROR)
        # 함수get()으로 처리하면 에러가 나오지 않고 none으로 리턴되어 처리가능
        # print( request.form.get('ori1') ) # Keyerror 뜨는것확인가능
        oriTxt = request.form.get('ori')
        if not oriTxt:
            return {'code':0, 'lang':'', 'desc':'원문데이터 누락'}
        # 2. 언어 감지
        # 2-1. DB에 로그처리
        # 3. 응답
        return { 'code':1, 'lang':'en', 'desc':'영어' }
    if request.method == 'GET': # else:
        return render_template('index.html')

# 4. 서버가동
if __name__=='__main__':
    app.run(debug=True)