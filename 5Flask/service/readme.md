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

## mariaDB
- 다운로드
    ```py
    https://downloads.mariadb.org/mariadb/10.4.12/ # 최신 바로전 버전

    https://downloads.mariadb.org/interstitial/mariadb-10.4.12/winx64-packages/mariadb-10.4.12-winx64.msi/from/http%3A//mirror.terrahost.no/mariadb/ # MSI 64버전
    ```
- 비번설정화면에서 8자리 이상해야 나중에 AWS 에 연동시 동일하게 가능
    - [x] enable access from remote machines for 'root' user
    - [x] use UTF-8
- 나머지는 체크변동없이 설치완료시킴

## Mysql client(Maria DB)
```bash
# 비번입력후
create database python_db;
show databases;
# 생성 확인후 exit로 나가기 
```
## HeidiSQL
1. 세션이름 local
1. 암호입력 11111111
1. 저장 후 열기

- DB삭제후 복원해보기
    - python_db 우클릭해서 SQL로 내보내기
    - 파일에 SQL 파일 불러오기


- 최상단텝 query
    ```slq
        -- 용산구의 행정구역 경계 gps를 가져와라
        SELECT *  FROM tbl_gps WHERE gu_id = '1';
        -- 다음과 같은 명령문임
        SELECT *  FROM tbl_gps 
            WHERE gu_id = (
                SELECT gu_id FROM tbl_areas WHERE gu ='용산구'
                );
    ```