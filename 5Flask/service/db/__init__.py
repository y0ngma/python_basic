## pymysql을 이용하여 마리아디비 연동
# 서버로 요청이 들어왔을때, 디비쪽으로 쿼리가 필요시 해당기능을 제공함수 모음
import pymysql as pSql

# gu_id : 1~(서울시자치구 번호)
def selectAreaGps(gu_id):
    # 쿼리 수행
    # 다음은 pymysql을 검색해서 나온 예시를 참고 하여 맞게 수정
    # pSql.cursors.DictCursor : [ {}, {},]
    connection = pSql.connect(  host    ='localhost',
                                user    ='root',
                                password='1'*8,
                                db      ='python_db',
                                charset ='utf8mb4',
                                cursorclass=pSql.cursors.DictCursor )
    result = [] # try문 밖에서 result를 return하므로 전역변수로 지정
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = '''
                SELECT * FROM tbl_gps
                WHERE gu_id = %s;
            '''
            # %s -> '1' 와 같음 
            # query 수행 (SQL, 매개변수 튜플)
            cursor.execute(sql, (gu_id,))
            # 결과 집합을 가져온다 (one or all[{},{}])
            result = cursor.fetchall()
            # print(result)
    finally: # 무조건 실행되는 문
        if connection: # 따라서 연결시에만 접속해제
            connection.close()    
    return result

def selectAreaIndex(  ):
    connection = pSql.connect(  host    ='localhost',
                                user    ='root',
                                password='1'*8,
                                db      ='python_db',
                                charset ='utf8mb4',
                                cursorclass=pSql.cursors.DictCursor )
    result = []
    try:
        with connection.cursor() as cursor:
            sql = '''
                SELECT * FROM tbl_areas ORDER BY gu ASC;
            '''
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        if connection:
            connection.close()    
    return result

# for test
if __name__ == '__main__':
    # selectAreaGps(1)
    print(selectAreaIndex)