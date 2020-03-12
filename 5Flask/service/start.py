# flask 기본 구성
# 1. 모듈가져오기
from flask import Flask, render_template, request, jsonify
# entry 가 run.py일때는 다음과 같이
# from service.ml import detect_lang
from ml import detect_lang
from db import selectAreaGps, selectAreaIndex
import os
print('====================================', os.getcwd())
# 2. 플라스크 객체 생성
app = Flask(__name__)

# 3. 라우팅
@app.route('/test') # 데코레이터. 함수안의 함수
def test():
    return render_template('test.html')

@app.route('/')
def home():
    # 기본 지역정보를 최초 화면 구성시 반영하여 처리
    areas = selectAreaIndex()
    # 구 정보를 gus라는 키값으로 지정하여 렌더링시 전달하겠다
    return render_template('dom.html', gus = areas, default=2 )

@app.route('/getAreaGps') # 
def getAreaGps():
    # 파라미터 받는부분(get방식)
    gu_id =request.args.get('gu_id')
    print( gu_id )
    return jsonify( selectAreaGps( gu_id ) )
    # 데이터 추출
    # tmp = [ {'lat':37.55487682, 'lng':126.9696652}, {'lat':37.55487682, 'lng':126.9696652} ]
    # json으로 응답
    # 응답 데이터에 html이 없다 => 전문통신, 미들웨어서버, API서버
    # 무게중심이 client에 쏠림 : angularjs, reactjs, vue
    # return jsonify(tmp)

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
        lang, desc = detect_lang( oriTxt )
        # 2-1. DB에 로그처리
        # 3. 응답
        return { 'code':1, 'lang':lang, 'desc':desc }
    if request.method == 'GET': # else:
        return render_template('index.html')

# 4. 서버가동
    # run.py 를 실행하면, __name__ => 'start(파일명)' 이므로
    # 조건에 맞지 않아 run 되지 않음
if __name__=='__main__':
    app.run(debug=True)