# Python에서 db 연동하기 => 도커이용

#### 도커?
    - PC안에 가상 PC

### Docker툴박스 다운로드
https://github.com/docker/toolbox/releases    

## 진행 과정 
- 인스톨     
    - 1. 전부 체크 (깃 설치 안되어 있으면 체크 = 깔려있으면 pass )
    - 2. 위에서 아래로 3개 체크 


- Docker Quickstart Terminal     
    - 터미널 진입 or 시작
        - 시작시 ```docker-machine start```
        - yes 
        - 고래 아래 그림 뜨면 진행완료 
- 메모리 체크 
    - 적으면 도커를 종료하고 메모리값을 재 산정하고 진행 
        - 1GB(1024MB) => 8GB(8192MB) 변경 
- 도커 종료 
    - 툴박스에서 
    - ``` $docker-machine stop ```

``` Bash 

                        ##         .
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
           \______ o           __/
             \    \         __/
              \____\_______/

docker is configured to use the default machine with IP 192.168.99.100
For help getting started, check out the docs at https://docs.docker.com


Start interactive shell

admin@DESKTOP-THUUM3S MINGW64 /c/Program Files/Docker Toolbox

```

*주의 : virtual box에서 메모리를 4096으로 변경 후 설치

```Bash 
//오라클12c 설치//
- 오라클 이미지 검색 
$ docker search oracle-12c
$ docker pull truevoly/oracle-12c

- 이미지확인 => 5.7GB
$ docker images
```

```Bash 
// 최초 시작시 // 
- 컨테이너 만들기 
$ docker run --name oracle12c -d -p 32765:8080 -p 32764:1521 truevoly/oracle-12c
$ docker logs oracle12c (주기적으로 log를 확인하여 100%가 될때까지 기다려야됨.)
```

[데이터 베이스 접속 client 프로그램 설치]
<< 설치 순서 >>
[설치 순서_1](http://ihongss.com/zip/java8.zip)
jdk-8u211-windows-x64 => 다 ok 
[설치 순서_2](http://ihongss.com/zip/sqldeveloper.zip) => DB에 접속하는 프로그램 
sqldeveloper-19.2.0.206.2117-no-jre/sqldeveloper/sqldeveloper.exe 실행 => 하면 자바경로 입력해야해 
[설치 순서_3](http://ihongss.com/zip/oracle_client.zip)
instantclient_19_3 file > C 드라이브로 이동      
내피시 > 시스템 > 고급시스템 설정 > 환경변수     
시스템 path 편집  > C 드라이브로 이동된 instantclient_19_3를 경로로 잡아줌      


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


```py
#파이썬 비트 확인

import platform 

print(platform.architecture())
```

---
파이썬 bit에 맞게 instant-client파일 다운로드     
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

- docker에서 mariadb 설치

```Bash

#vagrant plugin install vagrant-disksize

Vagrant.configure("2") do |config|
config.vm.box = "ubuntu/bionic64"
config.vm.network "forwarded_port", guest: 3306, host: 3396 #mariadb
config.vm.hostname = "localhost"
config.ssh.insert_key = false
config.disksize.size = '50GB'

config.vm.provider "virtualbox" do |vb|
vb.name = "mariadb"
vb.gui = false
vb.cpus = 2
vb.memory = "8192"
end
end

> vagrant up

> vagrant ssh


OS 업데이트 및 필수 패키지 설치
$ sudo apt update
$ sudo apt upgrade -y
$ sudo timedatectl set-timezone Asia/Seoul

Docker 설치 이미지 리포지토리 키 가져오기
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

리포지토리 추가하는 부분
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

$ sudo apt install -y docker-ce docker-ce-cli containerd.io

vagrant를 docker그룹에 추가
$ sudo usermod -aG docker vagrant

exit

> vagrant reload

> vargant ssh

$ docker version

$ docker search mariadb

$ docker pull mariadb

$ docker run --name mariadb-01 -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 mariadb
```

```python
import pymysql  #conda install pymysql


# MySQL Connection 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', port=3346, db='test', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 

# SQL문 실행
sql = "select * from member"
curs.execute(sql)


# 데이타 Fetch
rows = curs.fetchall()
print(type(rows))

for tmp in rows:
    #print(type(tmp))
    print("{}-{}-{}-{}-{}".format(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]))

# print(rows)     # 전체 rows

# Connection 닫기
conn.close()

```