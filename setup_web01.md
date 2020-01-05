# Python에서 db 연동하기 => 도커이용

#### 도커?
    - PC안에 가상 PC

```Bash 
// 최초 시작시 // 
- 컨테이너 만들기 
$ docker run --name oracle12c -d -p 32765:8080 -p 32764:1521 truevoly/oracle-12c
$ docker logs oracle12c (주기적으로 log를 확인하여 100%가 될때까지 기다려야됨.)
```

```bash
//오라클//
- 오라클 사용자 정보 
user : system # 최고 관리자 => 계정을 만들수 있음 
password : oracle
SID : xe

- 오라클 접속  > 새로 만들기 
Name : 192.168.99.100_system # 도커가 가진 주소 
호스트 이름 :192.168.99.100
포트 : 32764
    => 완료 ( 도움말 위에 >>> 상태 : 성공 )
```

- system계정 생성 후 오라클 계정 생성
```sql
create user admin IDENTIFIED by 1234;
grant connect, resource, dba to admin;
```
=> 위코드 작성후 블록 다 잡고  명령문 실행 >> 커밋 

#### 사용자 계정 만들기     
    user  :admin    
    password : 1234    

---
#### 테이블 생성 
이름 : MEMBER
    - id ( 키를 가짐 - 제약조건 )
    - pw
    - name
    - age (유형 : number)
    - joindate (유형 : date)

데이터에서 회원을 만듬  임의로 3개 
다 작성 후 => 변경사항 커밋 클릭 


```bash
//재시작//
구동중인 컨테이너 실행 확인
$ docker ps -a
도커 실행 하기
$ docker start oracle12c

conda 라이브러리 설치
$ conda install cx_oracle

pip로 라이브러리 설치
$ pip install cx_Oracle
$ python -m pip install cx_Oracle => 위의 명령어 실패 시

//Docker종료시//
$ docker stop oracle12c
$ docker-machine stop
```

```Bash 
// 필요시 //
$ docker stop oracle12c => 옵션) 데이너 실행 중지
$ docker rm oracle12c => 옵션) 컨테이너 삭제
```

```$ curl http://www.example.com/```

    
[다운로드 위치 : 클릭](https://www.oracle.com/kr/database/technologies/instant-client/downloads.html)     
압축을 풀어서 c:\instantclient_18_5으로 이동     
[오류발생시 설치 : 클릭 ](https://support.microsoft.com/en-us/help/4032938/update-for-visual-c-2013-redistributable-package)




```py
# oracle
import cx_Oracle as oci #conda install cx_oracle

#아이디/암호@서버주소:포트번호/SID
# system
conn = oci.connect('system/oracle@192.168.99.100:32769/xe')
# user
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding="uft-8")
cursor = conn.cursor()  # cursor 객체 얻기
cursor.execute('SELECT id, title, content, userid, CAST(CREATED_AT AS DATE) FROM BLOG_POST')  # SQL 문장 실행
blog_list = cursor.fetchall() #[(),(),()] 포멧
print(blog_list)
#print(blog_list[2][4])

conn.close()
```
