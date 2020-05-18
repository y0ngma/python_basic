## docker에서 우분투 설치
```bash
# @도커로 하는거
docker pull ansible/ubuntu14.04-ansible

# 바로 시작하는 컨테이너 생성
docker run --name ubuntu14.04 -i -t ansible/ubuntu14.04-ansible

exit # 우분투 빠져나온다
```
## docker 실행
```bash
# start는 실행
docker start ubuntu14.04
# attach는 들어가기
docker attach ubuntu14.04
# 아니면 다음의 방법으로
docker exec -it ubuntu14.04 /bin/bash

sudo apt update
```
## 아나콘다 설치
```bash
# 다운받기위해 wget설치
sudo apt install wget
# 다운
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
# 설치
bash Anaconda3-2020.02-Linux-x86_64.sh
# PYTHONPATH 경로 문구뜨면 yes
source ~/.bashrc

# 주피터 환경설정파일 생성
jupyter notebook --generate-config
# jupyter 인식못하면 지우고 다시 설치 rm

## 암호 만들기
ipython
ln [1]: from notebook.auth import passwd
ln [2]: passwd()
Enter password: 1234 # 암호 입력
Verify password: 1234 # 암호 재입력
Out[2]: 'sha1:a1s2d3f4...' # 입력한 비밀번호 암호화
In[3]: exit()
# 복사한 암호
sha1:23710c802376:bc8ab38b693fcc2d3ca2b93a0e39e7a78ebc5141
```

## 아나콘다 환경설정
```bash
# 편집기 설치 (vim or nano 설치하세요)
# vim 단축키 : a 는 편집기/esc후 :wq저장후나가기
sudo apt install vim -y
sudo apt install nano
# nano버전 올려줘야 알트 쉬프트 3먹힘
apt upgrade nano
# 단축키
# https://mintnlatte.tistory.com/170

# 수정
nano ~/.jupyter/jupyter_notebook_config.py
############ 수정한적 없을때는 암호 바꾸고 맨윗줄에 다음을 추가해도됨 ############
c.NotebookApp.allow_origin = '*'
c.NotebookApp.ip = '192.168.99.100'
c.NotebookApp.notebook_dir = u'/root/jupyter-workspace'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha1:32db0263e0c8:df37371b76de954943c8f7d914ad989756a1ddcd'
c.NotebookApp.port = 8888
###########################################################################

# 외부 접속 허용하기
# 아이피 설정
048라인 : c.NotebookApp.allow_origin = '*'
# 윈도우에서 도커를 실행한 경우 192.168.99.100 
204라인 : c.NotebookApp.ip = '192.168.0.xxx'
# 작업경로 설정
# pwd 해서 작업경로 복사붙여넣기
266라인 : c.NotebookApp.notebook_dir = u'/root/jupyter-workspace'
# 266라인 : c.NotebookApp.notebook_dir = u'/home/jupyter-workspace'
# 시작 시 서버PC에서 주피터 노트북 창이 열릴 필요 없음
272라인 : c.NotebookApp.open_browser = False
# 비밀번호 설정
281라인 : c.NotebookApp.password = u'sha1로 시작하는 암호...'
 'sha1:32db0263e0c8:df37371b76de954943c8f7d914ad989756a1ddcd'
# 포트 설정
292라인 : c.NotebookApp.port = 8888

# 방화벽 열기(안해도됨)
sudo ufw allow 8888
```

## 최초 접속
- 설치된 컨테이너를 내아이디로 커밋(최초 복사) 
- docker login/logout
    1. docker commit (컨테이너명) (도커아이디)/(이미지명):태크명(생략가능)
    2. docker push 도커아이디/이미지명
    ```bash
    # root에 폴더생성
    mkdir ~/jupyter-workspace
    exit

    # docker commit 구울컨테이너명 만들이미지명
    docker commit ubuntu14.04 ubuntu14.04image

    # docker run -it -p 8888:8888 --name 새로돌릴컨테이너명 돌릴이미지명
    docker run -it -p 8888:8888 --name ubuntu1 ubuntu14.04image
    ```

## 최초 이후 접속시
- 컨테이너가 이미 있으므로
    ```bash
    docker start ubuntu1
    docker attach ubuntu1
    ```

## 쥬피터 접속
- 다음을 실행 후 chrome에서 192.168.99.100:8888 들어가서 비밀번호 1234 치면된다(최초1회만)
    ```bash
    jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root
    ```

## 설치된 다른 이미지 삭제
1. docker images
2. docker rmi 지우고싶은 IMAGE ID 입력
    - 단, 다른곳에서 참조중인것은 삭제 불가 할 수 있음.

## 우툰부의 vs code를 로컬에서 접속
1. 윈도우 vs code에서 필요 확장프로그램 설치
    - docker
    - remote development
1. 다음과 같이 폴더와 파일을 생성한다
    -   docker-compose.yml
    -   .devcontrainer(폴더명)
        -   docker-compose.yml
        -   devcontrainer.json
            - 다음내용을 붙여넣는다
        ```json
        {
        "name": "Python 3",
        "dockerComposeFile": [
        "../docker-compose.yml",
        "docker-compose.yml"
        ],
        "service": "test",
        "workspaceFolder": "/app",
        "settings":  {
        "python.pythonPath": "/usr/local/bin/python",
        "python.linting.flake8Enabled": true,
        "python.testing.pytestEnabled": true
        },
        "postCreateCommand": "apt-get update && apt-get install -y git && pip3 install flake8",
        "extensions": [
        "ms-python.python",
        "littlefoxteam.vscode-python-test-adapter"
        ]
        }
        ```

1. 완성한 도커의 컨테이너에 접속한후 윈도vs code에서
    - ctrl + shift + P
        - remote-containers :attach to running container
        - 현재 docker attach 컨테이너 인곳이 있어야함
        - 클릭하면 접속하는데 시간이 좀 걸린다

1. 우분투 vs code에서 
- Code runner
    - 간혹 Run 버튼이 없을경우에 사용된다.