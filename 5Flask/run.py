# febric3을 이용하여 리눅스 서버에 자동 셋업
# 리눅스, git, febric으로 작성된 스크립트
# 사용화시, 최초 셋업 및 업데이트 관리시 사용
###########################################
# 본파일은 엔트리 파일이다(수행 진입로)
# apache server
from service.start import app

if __name__ == '__main__' :
    #app.run(host='0.0.0.0', port=80, debug=True)
    app.run(debug=True)
