## 조언
``` bash
## 애자일 회고
인디언들이 말을 타고 세차게 달린다  
얼마나 빨리 달리는지, 말 갈기가 펄럭인다.  
그런데 이따금 언덕에 올라 서서는 잠시 달리기를 멈춘 채 뒤를 돌아본다.  

그토록 열심히 달리던 이들이 왜 선 것일까?  
자신의 영혼이 따라오는가를 보기 위함이란다.  

## 자신이 새로운것을 추가로 배울단계인지,  
## 배운것을 채득할 시간인지 회고 해보자.
```
## Docker를 왜 쓸까?
- 앞전에 배운 소스가 안돌아가는 현상 : 
    - 버전차이
    - 도커기반으로 만들면 해결 가능

## - 도커 기본 사용법
    http://pyrasis.com/Docker/Docker-HOWTO
    https://dataitgirls2.github.io/10minutes2pandas/

1. 도커 이미지 다운로드
    1. docker pull `mrsono0/base_project:eda`
    1. docker images 이미지 확인  
        mrsono0이라는 이름의 도커 아이디 레포지토리의 eda 라는 이미지

1. 이미지로 컨테이너 설치하기
    1. docker run --rm --name eda -itd -u vscode -p 8888-8889:8888-8889 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes mrsono0/base_project:eda 
    1. docker ps -a 실행중인 컨테이너  확인
    2. 

2. 토큰값 받아서 주피터렙 접속하기
    1. docker logs --tail 30 eda
    2. `192.168.99.100:8888`
    3. notebook 하나 text.ipynb 작업저장

3. 설치된 컨테이너를 내아이디로 커밋(최초 복사)
    1. docker commit eda(컨테이너명) y0ngma(도커아이디)/eda(이미지명):태크명(생략가능)
    2. docker images

4. 설치된 다른 이미지 삭제
    1. docker images
    2. docker rmi 지우고싶은 IMAGE ID 입력
        - 단, 다른곳에서 참조중인것은 삭제 불가 할 수 있음.

5. 푸쉬하기
    1. 나를 포함한 다른사람이 pull하여 내 이미지를 받을 수 있게 한다.
    2. docker push 도커아이디/이미지명

1. 다음날 실행하기
   1. docker run --rm --name eda -itd -u vscode -p 8888-8889:8888-8889 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes y0ngma/eda 


## setup

- numpy, pandas 설치
    ```bash
    pip install pandas numpy
    conda install pandas numpy
    # 윈도우에서 명령어의 경로 확인 방법
    where python
    ```
- 세팅
    - docker pull, run
    ``` bash
    # mrsono0 base_project 검색 - tag에서 eda 필터링
    https://hub.docker.com/r/mrsono0/base_project/tags?page=1&name=eda

    docker pull mrsono0/base_project:eda


    # 1. 도커 허브에 있는 이미지로 컨테이너 런 (최초 실행시)
    docker run --rm --name eda -itd -u vscode -p 8888-8889:8888-8889 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes mrsono0/base_project:eda 
    
    -v /C/Users/admin/yonglab/eda:/home/vscode/notebooks/eda 

    #   # 이미지      : 파일
        # docker run    :
        # --rm           : 컨테이너 끌때 컨테이너 자동 삭제          
        # --name         : 이름짓기 마음대로
        # -i             : interaction
        # -t             : tty
        # -d             : demon 백그라운드로 돌리기
        # -u 돌아가는 계정설정. vscode에서 돌림
        # -p 8888-8889:8888-8889 주피터노트북-vscode : vscode차용 포트범위. 후자는 컨테이너 내부
        # 8881-8882 등으로 전자의 번호 바꿀 수 있음 
        # -e JUPYTER_RUN=yes : 리소스가 딸릴때 비활성화=no 가능
        # -v            : 특정폴더 로컬(경로) 연결. 
        # 단, /C/User.. 표기유의.  
        # ../eda:/home/vscode/notebooks/eda 
        # eda라는 도커명 양단 일치 유리
        # 소스파일이 도커내부에만 있게 하여 관리하거나 (-v줄 삭제)
        # 외부로 빼내어 깃에 올려두는 방법 두가지를 선택하라.
    ```

## 로컬 쥬피터랩 접속하기
- 원하는 경로에서 Shift우클릭으로 Powershell 열기
    - `jupyter lab` 입력

## 온라인 쥬피터랩 접속하기
- docker logs --tail 30 eda
    ```bash
    docker ps -a
    # 실행 확인 후
    docker logs --tail 30 eda
    # 뒤에서부터 30줄 보여달라.
    # docker logs --head 50 eda 앞에서부터 50줄
        (base) C:\Project_git\Project01_Crawling\MiniProject01\project>docker logs --tail 30 eda
        vscode@9406f700bac8:/$ Error: could not find config file /etc/supervisord.conf
        For help, use /usr/bin/supervisord -h
        info  Server listening on http://0.0.0.0:8889 # 포트
        info    - No authentication
        info    - Not serving HTTPS
        generated new fontManager
        [I 09:54:05.426 LabApp] Writing notebook server cookie secret to /home/vscode/.local/share/jupyter/runtime/notebook_cookie_secret
        [W 09:54:05.445 LabApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
        [I 09:54:05.495 LabApp] [beakerx] enabled
        [I 09:54:07.169 LabApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
        [I 09:54:07.169 LabApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
        [I 09:54:08.850 LabApp] Serving notebooks from local directory: /home/vscode/notebooks
        [I 09:54:08.850 LabApp] The Jupyter Notebook is running at:
        [I 09:54:08.850 LabApp] http://9406f700bac8:8888/?token=5217fdc3b4c9995adbeeae90c18d05d6e901dbbe4574523b
        [I 09:54:08.851 LabApp]  or http://127.0.0.1:8888/?token=5217fdc3b4c9995adbeeae90c18d05d6e901dbbe4574523b
        [I 09:54:08.851 LabApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
        [C 09:54:08.855 LabApp]

            To access the notebook, open this file in a browser:
                file:///home/vscode/.local/share/jupyter/runtime/nbserver-13-open.html
            Or copy and paste one of these URLs:
                http://9406f700bac8:8888/?token=5217fdc3b4c9995adbeeae90c18d05d6e901dbbe4574523b
            # 맨 하단 token= 이후 번호 복사
            # 192.168.99.100:8888에 접속하여 토큰번호로 쥬피터렙 접속
            or http://127.0.0.1:8888/?token=5217fdc3b4c9995adbeeae90c18d05d6e901dbbe4574523b
    ```

## 쥬피터 렙 콘솔창
- 기본 명령어
    ```sql
        ls                              --현경로 파일확인
        ls -al                          --현경로 모든 파일확인

        cd ..                           --하위
        cd dest                         --상위
        cd ./folder1/dest               --현재에서부터 목표\

        mkdir newfolder                 --만들기

        sudo -i                         --루트계정으로(admin) 로그인
        exit                            --로그인한 루트 로그아웃
            예: vscode@6ad77634b826:/$ pwd
                /
                vscode@6ad77634b826:/$ sudo -i
                root@6ad77634b826:~# pwd
                /root
                root@6ad77634b826:~# exit
                logout
                vscode@6ad77634b826:/$ 
            
        --conda install xlwt라고 검색하여
        conda install -c anaconda xlwt  --공홈에서 추천해주는 명령 이용가능
        

    ```

- + 누른후 콘솔창아이콘 클릭

    ```sql
    --모든 파일 확인
        vscode@9406f700bac8:~$ ls -al 
        total 52
        drwxr-xr-x 1 vscode vscode 4096 Jan 29 10:46 .
        drwxr-xr-x 1 root   root   4096 Jan  9 23:11 ..
        -rw-r--r-- 1 vscode vscode  220 Apr 18  2019 .bash_logout
        -rw-r--r-- 1 vscode vscode 3526 Apr 18  2019 .bashrc
        drwxr-xr-x 5 vscode vscode 4096 Jan 29 09:54 .cache
        drwxr-xr-x 3 vscode vscode 4096 Jan 29 09:54 .config
        drwxr-xr-x 3 vscode vscode 4096 Jan 29 10:46 .jupyter
        drwxr-xr-x 1 vscode vscode 4096 Jan 11 21:46 .local
        -rw-r--r-- 1 vscode vscode  807 Apr 18  2019 .profile
    -- notebooks 확인 후
        drwxr-xr-x 2 vscode vscode 4096 Jan 29 09:54 notebooks

    -- 루트계정으로 경로변경
        vscode@9406f700bac8:~$ sudo -i
        root@9406f700bac8:~# pwd
        /root

    --cd 경로변경
        root@9406f700bac8:~# cd /home/vscode

        root@9406f700bac8:/home/vscode# ls -al
        total 52
        drwxr-xr-x 1 vscode vscode 4096 Jan 29 10:46 .
        drwxr-xr-x 1 root   root   4096 Jan  9 23:11 ..
        -rw-r--r-- 1 vscode vscode  220 Apr 18  2019 .bash_logout
        -rw-r--r-- 1 vscode vscode 3526 Apr 18  2019 .bashrc
        drwxr-xr-x 5 vscode vscode 4096 Jan 29 09:54 .cache
        drwxr-xr-x 3 vscode vscode 4096 Jan 29 09:54 .config
        drwxr-xr-x 3 vscode vscode 4096 Jan 29 10:46 .jupyter
        drwxr-xr-x 1 vscode vscode 4096 Jan 11 21:46 .local
        -rw-r--r-- 1 vscode vscode  807 Apr 18  2019 .profile
        drwxr-xr-x 2 vscode vscode 4096 Jan 29 09:54 notebooks

    --chown -R 체인지 오너
        root@9406f700bac8:/home/vscode# chown -R vscode:vscode ./notebooks
        root@9406f700bac8:/home/vscode# ls -al
        total 52
        drwxr-xr-x 1 vscode vscode 4096 Jan 29 10:46 .
        drwxr-xr-x 1 root   root   4096 Jan  9 23:11 ..
        -rw-r--r-- 1 vscode vscode  220 Apr 18  2019 .bash_logout
        -rw-r--r-- 1 vscode vscode 3526 Apr 18  2019 .bashrc
        drwxr-xr-x 5 vscode vscode 4096 Jan 29 09:54 .cache
        drwxr-xr-x 3 vscode vscode 4096 Jan 29 09:54 .config
        drwxr-xr-x 3 vscode vscode 4096 Jan 29 10:46 .jupyter
        drwxr-xr-x 1 vscode vscode 4096 Jan 11 21:46 .local
        -rw-r--r-- 1 vscode vscode  807 Apr 18  2019 .profile
        drwxr-xr-x 2 vscode vscode 4096 Jan 29 09:54 notebooks
        root@9406f700bac8:/home/vscode# 
    ```

- cp:복사하기
```bash
docker cp ./a.py eda:/home/vscode/notebooks/
# cp(복사) SRC_PATH소스경로 DEST_PATH목표경로
# 현재 경로./에서 a.py(이름.확장자)를 eda의 다음경로로 
docker cp eda:/home/vscode/notebooks/pd01_boolseries.ipynb ./
# eda라는 컨테이너의 해당경로의 파일을 현재경로로 복사하라
# notebookS 철자 유의 
```
