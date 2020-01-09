## Table of Content
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
```
---

## Basic commands
- Oracle SQL Developer. 192.168.99.100_admin의 테이블에서
- 워크시트에 다음과 같이 입력하고 원하는 행을 드레그해서 개별실행 가능
- 실행결과는 중간의 '질의 결과'텝이나 상단의 BOARD_TABLE1의 데이터탭에서 확인 가능
    ```SQL
    1. 추가
        INSERT INTO BOARD_TABLE1(TITLE, CONTENT, WRITER, HIT, REGDATE)
        VALUES('sql에서 추가', '내용임', '작성자임', 34, SYSDATE);
        COMMIT;
        
    1. 삭제
        delete from board_table1 where no = 47;
        commit;
        
    1. 수정
        update board_table1 set title='변경1', content='변경2' where no = 52;
        update board_table1 set no=53 where no = 52;
        
    1. 조회;
        SELECT * FROM BOARD_TABLE1;
        SELECT * FROM BOARD_TABLE1 ORDER BY NO DESC;
        SELECT NO FROM BOARD_TABLE1 WHERE HIT >= 5;
        SELECT * FROM BOARD_TABLE1 WHERE NO IN (3, 4, 5, 6, 7, 8, 9);
        SELECT * FROM BOARD_TABLE1 UNION ALL;
            
        --SELECT * FROM WHERE NO (
        --    SELECT NO FROM BOARD_TABLE1 WHERE HIT >= 5
        --);
    ```

## 검색하는 방법(SELECT)
-     
    ```SQL
    - mysql 기준 1부터
        SELECT * FROM MEMBER_TABLE2 LIMIT 1,10;

    - oracle 에서 하는방법
        SELECT * FROM (
            SELECT 
                NO, TITLE, CONTENT, 
                ROW_NUMBER() OVER (ORDER BY NO DESC) ROWN
            FROM
                BOARD_TABLE1)
        WHERE ROWN BETWEEN 1 AND 10

    - 한글이 포함된 항목조회
        SELECT * FROM BOARD_TABLE1
        WHERE NAME LIKE '%'||'홍길동'||'%'
        WHERE TITLE LIKE '%'||'제목'||'%'
    ```
- 반별
    ```SQL
    
    SELECT
        'MEMBER_TABLE2'.'CLASSROOM', # [테이블]의 [클래스룸이라 저장된 데이터]랑
        SUM('MEMBER_TABLE2'.'KOR') AS 'SUM1', # kor행 데이터합 별칭을 SUM1로
        SUM('MEMBER_TABLE2'.'ENG') AS 'SUM2',
        SUM('MEMBER_TABLE2'.'MATH') AS 'SUM3'
    FROM 'MEMBER_TABLE2'
    ```

    