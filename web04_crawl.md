# DB

## DBMS
- 관계형 DB
- column을 미리 짜서 데이터를 맞춰 넣는다.
- 맞지 않는 데이터는 가짜데이터를 넣거나, column을 추가해야함
1. Oracle
1. my SQL
1. SQLite

## NOSQL
- 원래 먼저 이 방식으로 크롤링

1. tiny DB
1. Couch DB
1. mongoDB
    - mongo DB 설치하기
    ```bash
    $ docker-machine start # 먼저 컨테이너 구동.
    $ docker pull mongo
    $ docker search mongo # 이미지 검색
    $ docker images # 이미지 확인 364MB
        # 100% 완료되면
    - mongoDB 구축하기
    - https://robomongo.org/download
    - Download Robo 3T 최신버전 다운 (압축파일으로. 실행파일은 지저분해지므로)
    # -auth없으면 아무나 접속 가능
    $ docker run --name mongodb -d -p 32766:27017 mongo -auth 
    $ docker logs mongodb
        # 후에 Robo 3T connect-create 해보면 접속거부됨

    # -> 인증 없이 생성
    $ docker stop mongodb
    $ docker rm mongodb
    $ docker run --name mongodb -d -p 32766:27017 mongo
    $ docker start mongodb 
        # connect 하면 접속됨
    ```
1. robo3t.exe 실행
create 눌러서 다음을 입력한다.
address `192.168.99.100` : `32766`

1. html에서 정보 가져오기
@anaconda prompt
```bash
$ conda list beautifulsoup # 설치 확인
```

