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

## jQuery
    1. 요소(element)를 찾는다
    1. 그 요소에 이벤트를 준다. or 요소를 조작한다.
    1. 기타 통신처리(ajax)
- 크게 두가지로 나뉜다.
    - 통신
    - 돔조작
        - 찾기
            - 순서:id-클래스-부모자식관계-자식서열-특성속성
        - 이벤트 주기
        - 조작

## 1. MariaDB install
- 다운로드
    ```py
    https://downloads.mariadb.org/mariadb/10.4.12/ # 최신 바로전 버전

    https://downloads.mariadb.org/interstitial/mariadb-10.4.12/winx64-packages/mariadb-10.4.12-winx64.msi/from/http%3A//mirror.terrahost.no/mariadb/ # MSI 64버전
    ```
- 비번설정화면에서 8자리 이상해야 나중에 AWS 에 연동시 동일하게 가능
    - [x] enable access from remote machines for 'root' user
    - [x] use UTF-8
- 나머지는 체크변동없이 설치완료시킴

## 2. Mysql client(Maria DB)
    ```bash
    # 비번입력후
    create database python_db;
    show databases;
    # 생성 확인후 exit로 나가기 
    ```

## Maria 장점
- 테이블을 알아서 만들어준다
- csv -> DataFrame -> database에 insert(끝)


## DF -> SQL -> DB
- 업로드 준비하기
    ```py 
    # 설치 이 환경 : conda, 범용:pip
    ! conda install pymysql -y
    # 파이선에서 mysql계렬에 acess 할수 있는 모둘
    import pymysql
    # DataFrame에서 디비와 연동하기 위한 sql드라이버
    from sqlalchemy import create_engine
    # csv -> df
    import pandas as pd
    # df -> sql
    import pandas.io.sql as pSql # io는 input output
    # 연결
    db_url = 'mysql+pymysql://root:11111111@127.0.0.1/python_db'
    # 엔진생성
    engine = create_engine( db_url, encoding = 'utf8' )
    # 디비 연결
    conn = engine.connect()
    # 연결 및 자동해제
    ```
- 자료를 불러들여서 올리기
    ```py
    # 1. csv -> df 로 읽어서 변환
    df1 = pd.read_csv('./raws/gu.csv')
    with engine.connect() as conn:
        # 삽입
        # name 테이블명
        # if_exists: 기존데이터 있으면 덮어쓸것인지 추가할건지
        # index: 인덱스
        df1.to_sql( name ='tbl_areas', con=conn, if_exists='replace', index=False)
    df2 = pd.read_csv('./raws/gps.csv')
    with engine.connect() as conn:
        df2.to_sql( name ='tbl_areas', con=conn, if_exists='replace', index=False)
                
    ```

## HeidiSQL
1. 세션이름 local
1. 암호입력 11111111
1. 데이터베이스 : python_db 드롭다운 후 선택
1. 저장 후 열기

- DB삭제후 복원해보기
    - python_db 우클릭해서 SQL로 내보내기
    - 파일에 SQL 파일 불러오기


- 최상단 query텝
    ```sql
        -- 용산구의 행정구역 경계 gps를 가져와라
        SELECT *  FROM tbl_gps WHERE gu_id = '1';
        -- 다음과 같은 명령문임
        SELECT *  FROM tbl_gps 
        WHERE gu_id = (
            SELECT gu_id FROM tbl_areas WHERE gu ='용산구'
            );
    ```

## geoJson
- opinet.co.kr 에서 읍면동 까지 나누는 지도 참고
1. geoJson => 반정형
1. 디비오픈
1. 폴리곤 갯수만큼 반복
    - 행정구역별 (폴리곤단위) 한줄식 읽어서 (파일처리)
    - 읽은 데이터 한개는 json 형식이므로, json.load()
    - json.load() 자료구조를 그대로 유지
    - => gps, 기타 정보를 인덱싱 처리 가능
    - => df 구성 => db에 insert
        - 다만 시군별로 테이블 나눠서 넣기
        - 너무 느림 
1. 디비 닫기