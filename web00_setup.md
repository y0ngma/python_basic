## 웹환경구축
1. Set up Server
1. Connect DB
1. Register Admin
1. 


### Set up Server
- docker의 필요성 :
    ``` 개인 컴퓨터 사용을 깔끔하게 하고 서버 환경설정 관리를 용이하게 하기 위해 docker로 만든 container안에 Oracle을 설치하여 서버를 구축한다.
    ``` 
- 압축파일 풀고 모아둘 경로 C:\Programs of Develop 생성
- Docker 툴박스 다운로드
  - https://github.com/docker/toolbox/releases
  - 인스톨     
    - 전부 체크 (깃 설치 안되어 있으면 체크 = 깔려있으면 pass )
    - 위에서 아래로 3개 체크 
  - Docker Quickstart Terminal
    ```docker
    $ docker ps -a # 상태확인
     
                        ##         .
                  ## ## ##        ==
              ## ## ## ## ##    ===
          /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
          \______ o           __/
            \    \         __/
              \____\_______/
    $ docker-machine upgrade # 오류시
    ```
    - **주의** : virtual box에서 메모리를 4096으로(절반의양) 변경 후 설치
    
    - 오라클 버전 12c 설치하기
        ```docker
        $ docker search oracle-12c
        $ docker pull truevoly/oracle-12c
        인기있는 버전임. 
        $ docker images
        이미지 확인 5.7GB
        $ docker start oracle12c 
        $ docker-machine start
        ```
- Java 설치
  - 비트에 맞는 Java 다운로드
    - jdk-8u211-windows-x64
- SQL Developer
  - 압축을 C:\Programs of Develop 에 풀고 다음을 설정.  
  - 자바 설치경로 잡아주기
    - 기본설치경로 C:\Program Files\Java\jdk
- 오라클 클라이언트 다운로드
  - [오라클 홈페이지](https://www.oracle.com/kr/database/technologies/instant-client/downloads.html)
  - 압축을 C:\Programs of Develop 에 풀고 다음을 설정.
    ```
    내컴퓨터 우클릭> 시스템 > 고급시스템 설정 > 환경변수 > 아래의 시스템변수에서 path찾아 편집클릭 > instantclient_19_3 를 경로로 잡아줌
    ```
- DB Browser for SQLite


### Connect DB
- 
- 컨테이너 생성 (최초 1 회만)
    ```docker
    docker run --name oracle12c -d -p 32765:8080 -p 32764:1521 truevoly/oracle-12c
    docker ip # ip 주소 확인
    ```
    - 32765와 32764는 윈도우 port 번호
    - 8080과 1521은 docker container의 port 번호
    - oracle은 8080port에 설치된다. 그리고 윈도우의 32765port와 연결된다
    ```bash
    $ docker logs oracle12c 
    # 주기적으로 log를 확인하여 100%가 될때까지 기다려야됨
    docker ps -a  => 구동중인 컨테이너 확인
    ```
- docker container 구동 및 구동 중지
    ``` bash
    - docker start oracle12c # 컨테이너 구동
    - docker stop oracle12c # 옵션) 컨데이너 실행 중지
    - docker rm oracle12c # 옵션) 컨테이너 삭제
    ```

### Register Admin
- 서버를 구축하였으니 접속하기 위해 계정을 만든다.
    - sqldeveloper를 실행시킨다
    - 계정이 아직 없기 떄문에 최초로 로그인 할 때는, system 계정으로 접속하게 된다.
        ``` bash
        user : system # 최고 관리자 : 계정을 만들수 있음 
        password : oracle
        SID : xe
        ```
    - 새 계정을 생성한다
        ``` bash
        Name : 192.168.99.100_system # 도커가 가진 주소 
        호스트 이름 :192.168.99.100
        포트 : 32764
        # 완료시 ( 도움말 위에 >>> 상태 : 성공 )
        ```
        - sql 명령창에 다음 입력 
        ```sql
        CREATE user admin IDENTIFIED BY 1234; grant connect, resource, dba to admin;
        ```
        - 중요 : 위코드 작성후 ***블록 다 잡고***  명령문 실행 >> 커밋 

    - 사용자 계정 만들기     
        ``` bash
        user  :admin    
        password : 1234
        자동 로그인 설정하기    
        ```
    - 이후 system 계정 로그아웃하고 admin 계정으로 로그인 한다
        - 좌측의 TABLE이 system 계정일때보다 권한이 줄어든것 확인가능

- 테이블 생성 
    - 이름 : MEMBER
        - id ( 키를 가짐 - 고유 정보 )
        - pw
        - name
        - age (유형 : number)
        - joindate (유형 : date)

    - 데이터에서 회원을 만듬  임의로 3개 다 작성 후 => 변경사항 커밋 클릭 


### 웹 어플리케이션 생성
- anaconda prompt 에서
    ``` 
    $ cd C:\python_basic\2py_web\django\web1
    원하는 경로로 이동 후 다음을 입력
    ```
    ```
    웹 프로젝트 생성
    $ django-admin startproject web1
    
    웹 어플리케이션 생성
    $ django-admin startapp member
    
    생성된 모듈들을 확인 하면서 무엇이 있는지 전반적으로 파악하자
