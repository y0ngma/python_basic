# DB

## DBMS
관계형 DB  
column을 미리 짜서 데이터를 맞춰 넣는다.  
맞지 않는 데이터는 가짜데이터를 넣거나, column을 추가해야함

1. Oracle
    - datamodeler 압축풀고 .exe 실행
        `C:\Program Files\Java\jdk1.8.0_211`
    - 도식화하여 테이블을 그리고 데이터를 넣는 방식
    - 파일-임포트-데이터딕셔너리(ctrl shift B)-추가
    - 192.168.99.100_admin
    - 테스트 후 접속. - 생성한 계정클릭- 다음
    - 스키마/데이터베이스선택:admin 체크-다음. 
    - 임포트할 객체 선택
    - 예1:
        - 회원테이블 TABLE1
            - 아이디 pk
            - 전화번호
            - 주소 pk
                - 지역별로 서울고객, 부산고객 등 분류된 테이블 생성가능
        
        - 상품테이블(크롤링) ITEM1
            - 번호 pk
            - 가격
            
        - 거래내역 ORDER1
            - 주문번호 pk
            - 아이디 pk(만 알면 회원정보를 가져오게함:외래키)
                - 회원정보가 수정되어도 거래내역도 자동 갱신됨
                - 외래키 없이 주문자 정보 입력시 TABLE1에서 탈퇴한 회원도 거래내역에서는 탈퇴안한것처럼 됨.
                - 외래키사용시 주문내역추적하려면 원본회원정보 삭제불가(회원 탈퇴시)
            - 물품번호 pk
                - 마찬가지로 매진된 상품도 삭제하지 않고 0또는1로 표기 후 보관
            - 내용(내역서) : 구매자 번호와 구매상품 품번을 ORDER1(TABLE)에 넣기
                - 거래내역에 주문자와 주문상품 표시해주기
                ```SQL
                INSERT INTO ORDER1(MEM_NO,ITM_NO, REGDATE) VALUES(존재하는회원번호,존재하는상품번호, SYSDATE);-- 상품구매
                COMMIT; 
                ```
            
            - 가져오고자 하는 키값의 유형(number)랑 외래키 유형 일치필요
                - order1 테이블편집-좌측'제약조건'텝-(Alt 1)새 제약조건
                - 새 외래키 제약조건
                - 테이블    : 가져올 테이블 (TABLE1)
                - 제약조건  : TABLE1_PK 
                - 로컬 열   : MEM_NO
            
            ```sql
            SELECT * FROM ITEM1 t4
            INNER JOIN
                (SELECT * FROM TABLE1 t1
                INNER JOIN ORDER1 t2
                ON t1.no = t2.mem_no) t3 
                --WHERE 회원.번호 = 상품.회원번호
            ON t4.no = t3.itm_no;    
            ```          

    - 예 검색어:
        -       
    - 좌측상단 커서 누른후 드래그-우클릭 DDL(테이블정의어)미리보기 가능
    - 파일-보고서-보고서생성(pdf등) 하여 출력가능
1. my SQL
1. SQLite
---

## NOSQL
- 원래 먼저 이 방식으로 크롤링

1. tiny DB
1. Couch DB
1. mongoDB
    1. mongo DB 설치하기
        ```bash
        $ docker-machine start # 먼저 컨테이너 구동.
        $ docker pull mongo
        $ docker search mongo # 이미지 검색
        $ docker images # 이미지 확인 364MB
            # 100% 완료되면
    
    1. mongoDB 구축하기
        ```bash
        # -auth없으면 아무나 접속 가능
        $ docker run --name mongodb -d -p 32766:27017 mongo -auth 
        $ docker logs mongodb
            # 후에 Robo 3T connect-create 해보면 접속거부됨

        # -> 인증 없이 생성위해 기존것 삭제
        $ docker stop mongodb
        $ docker rm mongodb
        
        $ docker run --name mongodb -d -p 32766:27017 mongo
        $ docker start mongodb 
            # connect 하면 접속됨
        ```
    
    1. Robo 3T (sql 처럼 DB 관리)
        - https://robomongo.org/download
        - Download Robo 3T 최신버전 다운 (압축파일으로. 실행파일은 지저분해지므로)
        - robo3t.exe 실행
            - create 눌러서 다음을 입력한다.
            - address `192.168.99.100` : `32766`
- Crawling
1. Beautiful Soup
    @Anaconda Prompt
    ```bash
    $ pip install pymongo
    
    # html에서 정보 가져오기
    $ conda list beautifulsoup # 설치 확인
    ```
1. 크롤링
    서버와 그롤링
    html, json, xml, csv
    로그인 이후 페이지, 자바스크립트 페이지

    드라이버를 제공하는 크롬 등을 통해 클릭 자동화등 구현
    파이썬에서 보기 위해 driver 설치
        크롬 도움말-버전확인

---