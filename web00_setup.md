## 웹환경구축

### 서버 구축
- 압축파일 풀고 모아둘 경로 C:\Programs of Develop 생성
- Docker 툴박스 다운로드
  - https://github.com/docker/toolbox/releases
  - 인스톨     
    - 전부 체크 (깃 설치 안되어 있으면 체크 = 깔려있으면 pass )
    - 위에서 아래로 3개 체크 
  - Docker Quickstart Terminal
    ```bash
    $ docker ps -a 
      상태확인
    $ docker start oracle12c 
    $ docker-machine start 
      실행완료시 다음 출력됨
                        ##         .
                  ## ## ##        ==
              ## ## ## ## ##    ===
          /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
          \______ o           __/
            \    \         __/
              \____\_______/
    ```
  - 오라클 버전 12c 설치하기
    - **주의** : virtual box에서 메모리를 4096으로 변경 후 설치
    ```bash
    $ docker search oracle-12c
    $ docker pull truevoly/oracle-12c
    인기있는 버전임. 
    $ docker images
    이미지 확인 5.7GB
    ```
- Java 설치
  - 비트에 맞는 Java 다운로드
    - jdk-8u211-windows-x64
- SQL Developer
  - 압축을 C:\Programs of Develop 에 풀고 다음을 설정.  
  - 자바 설치경로 잡아주기
    - 기본설치경로 C:\Program Files\Java
- 오라클 클라이언트 다운로드
  - [오라클 홈페이지](https://www.oracle.com/kr/database/technologies/instant-client/downloads.html)
  - 압축을 C:\Programs of Develop 에 풀고 다음을 설정.
    ```
    내컴퓨터 우클릭> 시스템 > 고급시스템 설정 > 환경변수 > 아래의 시스템 path 편집 > instantclient_19_3 를 경로로 잡아줌
    ```
- DB Browser for SQLite

  
