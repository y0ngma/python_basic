## 주제
- 웹기반 머신러닝을 활용하여 언어감지 기능을 제공하는 서비스

## 프로젝트구조
```py
/
L run.py        # entry point : 시작점
L read.me       # 설명파일
L service       
    L start.py  # 플라스크 라우팅, 서버설정
    L ml
        L __init__.py                # 머신러닝 모듈작동
        L clf_labels.json            # 분류의 답을가진파일
        L clf_model_yyyymmddhhmm.model  # 학습된 SVC
    L static            # 정적파일(*.js,*.css,리소스등)
    L templates         # 랜더링할 html파일위치
        L index.html    # 서비스 메인화면
```