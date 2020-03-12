# 언어감지 예측 모델기능으로 학습된 알고리즘을 로드
# 요청이 들어올때마다 예측하고 결과를 던져준다
from sklearn.externals import joblib
import json, re
# import os
# 경로 (entry + 프로젝트위치까지 고려 기준으로 경로설정)
# model_path = os.getcwd()+'/service/ml/clf_modle_202003101113.model'
# label_path = os.getcwd()+'/service/ml/clf_labels.json'
model_path = './service/ml/clf_model_2020031101113.model'
label_path = './service/ml/clf_labels.json'
# 분류기(알고리즘)
clf = joblib.load( model_path )
# 레이블(정답) 로드
with open(label_path, 'r') as f:
    clf_label = json.load(f)

# 입력: 원문 텍스트
def detect_lang( oriTxt ):
    # 주피터파일을 참고하여 구현하시오
    # 1. 데이터 가공
    # freq[1]['freqs'] => [ [1,2,...7] ]=>(1,26)
    
    # 1-1. 원문 -> 전처리(영어만, 소문자로)
    text = transLowerAlpha(oriTxt)
    # 1-2. 빈도계산 -> 정규화->[[]]
    counts = [ 0 for n in range(26) ]
    ASCII_A = ord('a')
    for ch in text:
        counts[ (ord(ch)-ASCII_A) ] += 1
    frequences = list( map( lambda x:x / len( text ), counts ) ) 
    # [[]]
    data = [ frequences ]
    # 2. 예측
    predict = clf.predict( data )
    # predict => ['en']
    # 3. 출력결과 구성
    return predict[0], clf_label[ predict[0] ] 
    # 출력 : (감지된 언어코드, 언어코드의 한글명)
    # return 'en', '영어'

def transLowerAlpha( rawText ):
    # 원문 -> 전처리(영어만, 소문자로)
    text = rawText.lower()           # 소문자처리
    p    = re.compile('[^a-z]*')    # 정규식정의.소문자제외 전부
    return p.sub( '' ,  text )     # 소문짜빼고 전부 치환