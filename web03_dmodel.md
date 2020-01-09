# Django WEB 
## Index
- 개발 환경
    - 파이썬, 장고, 데이터 베이스
        1. 파이썬 설치
        2. 장고 설치
        3. 데이터베이스 설치
                - SQLite(추천)
            - 메모리에 상주하는 프로세스 없이 파일 하나에 데이터베이스를 저장 
        4. 장고 프로젝트 만들기
            - Step01
                - 터미널 => ``` $ django-admin.py startproject 프로젝트이름```
                - 현재 디렉터리에 '프로젝트이름'을 만들고 기본파일 자동 설치
            - Step02
                - Web 요소 구성하기  
                - 어플리케이션 생성 (여러개 생성 가능)   
                    - Board, Member 앱 생성     
                - Django 서버 구동(http://127.0.0.1:8000/) 
            - Step 03
                - Member 기능 추가 
                    - INDEX, LOGIN, Singin 페이지 등등 생성
        - django model
            - sql문 없이 구동

### django model

```SQL
DDL
테이블 정의어
    CREATE      # 생성
    ALTER       # 타입을 변경
    DROP        # 삭제
    RENAME      # 이름
    TRUNCATE    # 비우기

DML
데이터 조작어
    UBSERT 
        INTO MEMBER(ID, NAME, AGE) VALUEs('a', 'b', 34) # VALUES 철자주의
    UPDATE
        MEMBER SET NAME='B1', AGE=44 WHERE ID='a' 
    DELETE
        FROM MEMBER WHERE ID='a'
    SELECT
        * FROM MEMBER WHERE ID LIKE 'a%'    # LIKE 는 정규식
        ORDER BY NO DESC | ACS              # 내림 | 오름차순
    "%" || "가" ||"%"   -> "가" 포함
    "가"|| "%"          -> "가" 시작
    "%" || "가"         -> "가" 끝남

   

DCL 
데이터 제어어
    GRANT       # 권한 부여
    REVOKE      # 권한 삭제

TCL
트랜잭션 제어어
    COMMIT      # 적용
    ROLLBACK    # 포인트로 돌아가기
    SAVEPOINT