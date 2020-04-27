# 목표
- Virtual Box로 가상 분할 된 우분투 각각 도커내 하둡 데이터노드 포트세팅해서 외부 마스터노드에서 연결 및 스파크로 운영

# 순서
>1. Virtual Box에서 우분투 설치
>1. 우분투 포트 설정
>1. MobaXterm에 포트 연결
>1. 하둡
>1. 스파크 : 실시간, 빅데이터
>1. 아나콘다 주피터
>1. pyspark


# 1. Virtual box
- 우분투 18.04 다운로드 (2GB)
    `https://ubuntu.com/download/desktop/thank-you?version=18.04.4&architecture=amd64`
1. 새로만들기
    - 이름 적고 다음
1. 메모리 **4기가** 할당
1. 지금 새 가상 하드디스크 만들기
1. VDI
1. 동적할당
1. **30기가** 할당 - 만들기
    - 실패시 우클릭 삭제 가능
1. 우클릭 - 설정
1. @ 네트워크 텝 (네트워크 연결하기)
    - 다음에 연결됨 : 어댑터에 브리지 선택
    - 무작위모드 : 가상머신에 허용 선택
1. @ 저장소텝 (시디설치)
    - 컨트롤러 IDE 의 우측 왼쪽 아이콘(다운받은 iso 광학드라이브추가)
    - 선택후 확인
1. @메인화면
    - 시작버튼의 드롭다운 (화살표버튼) 클릭
    - 때낼 수 있도록 시작 클릭
    - 한글 선택후 설치하기
    - 일반설치, 업데이트 다운로드 선택후 계속
    - 디스크를 지우고 설치 클릭
        - 이름 : user1
        - 컴퓨터이름 : user1-VirtualBox
        - 사용자이름 : user1
        - password : 1234
        - 자동으로 로그인
    - 설치완료

# 2. 우분투
- ctrl + alt + t 해서 cmd 창에서
    ```py
    sudo apt update -y # 업데이트
    sudo apt install net-tools # 서버주소 확인
    ifconfig # 서버 ip 주소 확인
    #######################################
    sudo apt install ssh -y # ssh 프로그램 설치
    sudo service ssh start  # ssh 구동
    sudo ufw enable # 방화벽 활성화
    sudo ufw allow 22 # 방화벽 22번 열기
    sudo ufw status # 방화벽 확인
    #######################################

    ```

# 3. MobaXterm 
## 다운로드
- `https://mobaxterm.mobatek.net/download-home-edition.html`
- Free download
    - Portable edition v20.2
- 좌측상단 session 클릭
    - ssh 클릭
        - Remote host에 `@우분투cmd ifconfig로 확인한 주소` 입력

## 서버주소로 이름 변경
- @ MobaXterm cmd
    ```py
    # @cmd 
    hostname # 현재 이름 : user1-virtualbox를 ip주소로 변경
    sudo nostnamectl set-hostname 192.168.0.15
    hostname # 192.168.0.15로 변경 확인
    sudo reboot # 재접속시 user1/1234로 로그인
    sudo apt install openjdk-8-jre-headless -y
    sudo apt install openjdk-8-jdk-headless -y

    java -version # 1.8.0_242
    pwd # home/user1
    ```


# 4. 하둡
- start-all.sh
## 4.1 다운로드
- @ MobaXterm cmd
    ```py
    # @크롬에서 http://apache.tt.co.kr/hadoop/common/hadoop-3.1.3/
    # @페이지에서 마지막 hadoop-3.1.3.tar.gz우클릭 링크주소복사
    # @MobaXterm 에서
    wget 링크주소 붙여넣기 
    ls
    tar -zxvf hadoop-3.1.3.tar.gz # 압축풀기
    ls
    ```

## 4.2 하둡 환경 설정
- @ MobaXterm cmd
    ```py 
    # 환경설정 파일
    nano ~/.bashrc
    # 가장 밑으로 이동후 복사
    export HADOOP_HOME=/home/user1/hadoop-3.1.3
    export HADOOP_COMMON_HOME=/home/user1/hadoop-3.1.3
    export HDFS_NAMENODE_USER="user1"
    export HDFS_DATANODE_USER="user1"
    export HDFS_SECONDARYNAMENODE_USER="user1"
    export YARN_RESOURCEMANAGER_USER="user1"
    export YARN_NODEMANAGER_USER="user1"
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$JAVA_HOME/bin
    # 저장 ctrl + S 후 나오기 ctrl + X
    ```
- 환경변수 변동사항 적용 
    ```py
    # 수정된 환경변수를 적용
    source ~/.bashrc
    ``` 
- 여러 환경변수 수정하기
    - 경로 `~/hadoop-3.1.3/etc/hadoop/` 에서 직접 열어서 수정하거나 nano 이용
    ```py
    # 1 #######################################################
    nano ~/hadoop-3.1.3/etc/hadoop/hadoop-env.sh
    # @54라인 
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 

    # 2 ########################################################
    nano ~/hadoop-3.1.3/etc/hadoop/core-site.xml
    # 마지막줄에 추가
    <configuration>
        <property>
            <name>fs.default.name</name>
            <value>hdfs://192.168.0.XXX:9000</value> ### 자신 주소
        </property>
    </configuration>

    # 3 #######################################################
    nano ~/hadoop-3.1.3/etc/hadoop/hdfs-site.xml
    # 마지막줄에 추가
    <configuration>
        <property>
            <name>dfs.namenode.name.dir</name>
            <value>/home/vagrant/hadoop-3.1.3/data/nameNode</value>
        </property>

        <property>
            <name>dfs.datanode.data.dir</name>
            <value>/home/vagrant/hadoop-3.1.3/data/dataNode</value>
        </property>

        <property>
            <name>dfs.replication</name>
            <value>1</value>
        </property>
    </configuration>

    # 4 #######################################################
    nano ~/hadoop-3.1.3/etc/hadoop/mapred-site.xml
    # 마지막줄에 추가
    <configuration>
        <property>
            <name>map.framework.name</name>
            <value>yarn</value>
        </property>
    </configuration>

    # 5 #######################################################
    nano ~/hadoop-3.1.3/etc/hadoop/yarn-site.xml
    # 마지막줄에 추가
    <configuration>
        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
        </property>
    </configuration>

    # 6 #######################################################
    # 네임노드 데이터노드 디렉토리 생성
    mkdir -p ~/hadoop-3.1.3/data/nameNode
    mkdir -p ~/hadoop-3.1.3/data/dataNode
    ```

## 4.3 하둡접속 설정
### 인증키 등록
#### 파일생성
- ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
    ```py
    (base) user1@192:~$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
    Generating public/private rsa key pair.
    Created directory '/home/user1/.ssh'.
    Your identification has been saved in /home/user1/.ssh/id_rsa.
    Your public key has been saved in /home/user1/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:rcmUeG4JhSiqjOjbz9j+eN2LWi8vxZ/vPAknln/NxCM user1@192.168.0.15
    The key's randomart image is:
    +---[RSA 2048]----+
    |                 |
    |     . .         |
    |  . . . .        |
    | . .   o o       |
    |.     o S o   .. |
    |=      * + o E oo|
    |+.      O.o o Bo+|
    |. . + .o.+o. o.++|
    | o.oo*oo..++. o+o|
    +----[SHA256]-----+
    ```
#### 파일내용 복사
- cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
#### 0600 권한변경
- chmod 0600 ~/.ssh/authorized_keys
#### 암호없이 접속되는지 확인
- ssh localhost
    ```py
    (base) user1@192:~$ ssh localhost
    The authenticity of host 'localhost (127.0.0.1)' can't be established.
    ECDSA key fingerprint is SHA256:wcGfWumdcn963uMbemddWHdx0JUPUZ03+mWIE/DSZYo.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added 'localhost' (ECDSA) to the list of known hosts.
    Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 5.3.0-46-generic x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage


    * Canonical Livepatch is available for installation.
    - Reduce system reboots and improve kernel security. Activate at:
        https://ubuntu.com/livepatch

    패키지 0개를  업데이트할 수 있습니다.
    0 업데이트는 보안 업데이트입니다.

    Your Hardware Enablement Stack (HWE) is supported until April 2023.
    Last login: Tue Apr 21 13:17:43 2020 from 192.168.0.65
    ```

#### name노드 포멧
- hdfs namenode -format
- start-all.sh
- jps
    ```py
    7377 NameNode
    8537 Jps
    8042 ResourceManager
    7580 DataNode
    7822 SecondaryNameNode
    8222 NodeManager
    ```

#### 방화벽 허용
- sudo ufw allow 9000
- sudo ufw allow 9870
- sudo ufw allow 9864
- sudo ufw allow 9866

## 4.4 접속
### 크롬에서 접속 확인해보기
- 크롬에서 192.168.0.`XXX`:9870 으로 이동
    - @ Utilities텝
        - Browser the file system 이 파일 저장소
    ```py
    hdfs dfs -ls  # 없음
    hdfs dfs -mkdir /test1  # 하둡 파일시스템에 폴더 생성 
    hdfs dfs -chmod -R 777 /test1  #  /test1의 권한을 모든 사용자가 사용할 수 있게
                    # R 하위경로에 대한 권한 범위
                    # 777 뜻 (모든사용자 모든 권한)
                        # 744, 755 많이 씀
    ```
       
    비고|주사용자|그룹|일반인
    --|--|--|--
    권한여부|Read<br>Write<br>Execute|Read<br>-<br>Execute|Read<br>-<br>- 
    이진수|111|101|100
    십진수|7|5|4

***************************************************

### 접속 실패시
-
    ```py
    # 1. 프로세스 중지
        stop-all.sh

    # 2. jps로 확인

    # 3. 환경설정 다시확인

    # 4. 데이터노드 네임노드의 폴더안의 파일 지우기
        rm -rf ~/hadoop-3.1.3/data/nameNode
        rm -rf ~/hadoop-3.1.3/data/dataNode

        mkdir -p ~/hadoop-3.1.3/data/nameNode
        mkdir -p ~/hadoop-3.1.3/data/dataNode

    # 5. name노드 포멧
        hdfs namenode -format
        start-all.sh

    # 6. jps
        7377 NameNode
        8537 Jps
        8042 ResourceManager
        7580 DataNode
        7822 SecondaryNameNode
        8222 NodeManager
    ``` 

### 케이블연결 실패시
- 공유기 하나에 여럿이 물려 있는 환경에서는 자동으로 포트번호가 바뀌므로 수동으로 이를 고정하는 방법
- @케이블연결 설정 
    - IPv4 
        - 본인아이피 : 192.168.0.xxx
        - 네트마스크 : 255.255.255.0
        - 게이트웨이 : 192.168.0.1
        - 네임서버DNS : 168.126.63.1
            - DNS란, naver.com의 번호로된 주소명 따위



# 5. 아나콘다 3
## 5.1 다운로드
- 공식홈페이지에서 링크 얻어서 다운
    ```py
    # 설치중에 홈텝에서 주소 더블클릭해서 창하나 더 열기
    # 아나콘다 리눅스버전 64비트 다운로드버튼 우클릭 링크주소복사
    wget 우클릭 붙여넣기
    ls # 다운로드완료 후 확인
    bash Anaconda3-2020.02-Linux-x86_64.sh # yes 두번
    source ~/.bashrc # "~" = home/사용자
    # rm -rf ~/anaconda3 # 아나콘다 삭제하기
    ```

## 5.2 세팅
- 주피터환경설정파일생성
1. jupyter notebook --generate-config 
2. ipython

    ```py
    # 비번 만들기
    In [1]: from notebook.auth import passwd
    In [2]: passwd()
        Enter password:1234
        Verify password:1234
    Out[2]: 'sha1:34bce7558629:ddac31e930a75c661c4b617f3277a15cd03cc120'
    In [3]:exit() # 위 비번을 복사해둔다.
    ```

3. 환경설정
    ```py
    nano ~/.jupyter/jupyter_notebook_config.py
    # alt + shift + 3 = 행번호 표시
    # ctrl + / + 행번호 = 이동
    # 다음을 수정 후 ctrl + S 저장
    048라인 : c.NotebookApp.allow_origin = '*'  # 외부 접속 허용하기
    204라인 : c.NotebookApp.ip = '10.0.2.15'  #아이피 설정
    266라인 : c.NotebookApp.notebook_dir = u'/home/user1/jupyter-workspace' #작업경로 설정
    272라인 : c.NotebookApp.open_browser = False # 시작 시 서버PC에서 노트북 창이 열릴 필요 없음
    281라인 : c.NotebookApp.password = u'sha1로 시작하는 암호...' # 비밀번호 설정
    292라인 : c.NotebookApp.port = 8888   #포트 설정
    # 저장 후 
    sudo ufw allow 8888 # 방화벽 열기
    mkdir ~/jupyter-workspace # 폴더생성
    jupyter notebook --config ~/.jupyter/jupyter_notebook_config.py # 크롬에서 192.168.0.15:8888 접속 확인
    ```



# 6. 스파크
- start-master.sh
- start-slave.sh spark://127.0.0.1:7077
## 6.1 설치 
    ```py
    start-all.sh
    sudo apt install scala -y

    wget http://apache.tt.co.kr/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz

    tar -xzvf spark-2.4.5-bin-hadoop2.7.tgz
    ```

## 6.2 설정
    ```py
    nano ~/.bashrc
    # 아랫줄에 추가
    export SPARK_HOME=/home/user1/spark-2.4.5-bin-hadoop2.7
    export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
    ```

## 6.3 환경변수 설정
- 경로 `/home/user1/spark-2.4.5-bin-hadoop2.7/conf/`
    ```py
    # 해당경로로 이동해서
    cd ~/spark-2.4.5-bin-hadoop2.7/conf
    #########################################################
    ### 1. copy [복사할.파일.template] [복사할-이름]
    cp spark-env.sh.template spark-env.sh
    # 복사된 spark-env.sh 수정
    nano spark-env.sh
    # 마지막줄에 추가
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export HADOOP_HOME=/home/user1/hadoop-3.1.3
    export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
    export LD_LIBRARY_PATH=$HADOOP_HOME/lib/native
    export SPARK_LOCAL_IP="192.168.0.XXX"  # => local ip
    export PYSPARK_PYTHON=/home/user1/anaconda3/bin/python3
    export PYSPARK_DRIVER_PYTHON=/home/user1/anaconda3/bin/python3
    export SPARK_MASTER_HOST="192.168.0.XXX"  # => remote access ip
    export SPARK_WORKER_INSTANCES=1
    export SPARK_WORKER_MEMORY=4096m
    export SPARK_WORKER_CORES=8
    export SPARK_MASTER_OPTS="-Dspark.deploy.defaultCores=5"

    #########################################################
    ### 2. 파일 복사
    cp spark-defaults.conf.template spark-defaults.conf
    # 복사된 spark-defaults.conf 수정
    nano spark-defaults.conf
    # 마지막줄에 추가
    spark.master                spark://127.0.0.1:7077
    spark.executor.instances    1
    spark.executor.cores        3
    spark.executor.memory       4g
    spark.driver.cores          1
    spark.driver.memory         4g
    ```


## 마스터/슬레이브 실행
    ```py
    # 방화벽열기
    sudo ufw allow 7077
    # spark 마스트 구동
    start-master.sh
    # spark 슬레이브 구동
    start-slave.sh spark://127.0.0.1:7077

    jps # 확인해보기 
    4349 Jps
    3434 NodeManager
    3243 ResourceManager
    2538           NameNode
    3009 Secondary NameNode
    2727           DataNode
    4262 Master            # 추가 됨.
    4314 Worker            # 추가 됨.
    # 4965 SparkSubmit      # spark를 실행하였으므로
    ```
- pyspark 설치
    ```py
    # pip install pyspark 
    conda install -c conda-forge pyspark

    # 터미널을 1개더 추가로 접속
    jupyter notebook
    # 크롬에서 http://192.168.0.XXX:8888
    ```

# 7. Docker
## 7.1 설치
- 이미지 리포지토리 키 가져오기
    ```py
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    # 리포지토리 추가하는 부분
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    
    sudo apt install -y docker-ce docker-ce-cli containerd.io

    # 현재 user1은 도커 포트 진입 불가 하므로 docker그룹에 추가
    sudo usermod -aG docker user1

    #리부팅
    docker -v
    docker search mariadb
    docker pull mariadb
    docker run --name mariadb-01 -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 mariadb
    docker container ls -a
    docker exec -it mariadb-01 bash => mariadb-01컨테이너로 진입

    ```
- 우분투에 도커 설치
    ```py
    # Docker 설치 이미지 리포지토리 키 가져오기
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    # 리포지토리 추가하는 부분
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    
    sudo apt install -y docker-ce docker-ce-cli containerd.io

    # docker그룹에 추가
    sudo usermod -aG docker user1

    # 리부팅
    sudo reboot 
    ```
- tensorflow 설치
    ```py
    docker search tensorflow
    # https://www.tensorflow.org/install/docker?hl=ko

    docker pull tensorflow/tensorflow:latest-gpu-py3-jupyter
    # docker로부터 tensorflow를 pull하는데 /
    # latest버전-gpu엔진-py3파이선버전을-jupyter으로 돌리겠다
    ```

- tensorflow를 사용방법
    ```py
    # 방화벽
    sudo ufw allow 8889
    # 
    docker run -it --name tf01 -d -p 8889:8888 tensorflow/tensorflow:latest-gpu-py3-jupyter
    # -it : attach
    # --name tf01 
    # -d : 백그라운드 
    # -p 8889:8888 : 기존 8888을 8889에 연결해서 접속
    ```

- 토큰번호 확인하기
    ```py
    # 하단에 생성되는 토큰 번호를 포함하여 쥬피터 실행 혹은 쥬피터에서 토큰번호 직접 입력하게된다
    (base) user1@192:~$     docker logs tf01

    ________                               _______________
    ___  __/__________________________________  ____/__  /________      __
    __  /  _  _ \_  __ \_  ___/  __ \_  ___/_  /_   __  /_  __ \_ | /| / /
    _  /   /  __/  / / /(__  )/ /_/ /  /   _  __/   _  / / /_/ /_ |/ |/ /
    /_/    \___//_/ /_//____/ \____//_/    /_/      /_/  \____/____/|__/


    WARNING: You are running this container as root, which can cause new files in
    mounted volumes to be created as the root user on your host machine.

    To avoid this, run the container by specifying your user's userid:

    $ docker run -u $(id -u):$(id -g) args...

    [I 05:58:11.994 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
    jupyter_http_over_ws extension initialized. Listening on /http_over_websocket
    [I 05:58:12.260 NotebookApp] Serving notebooks from local directory: /tf
    [I 05:58:12.260 NotebookApp] The Jupyter Notebook is running at:
    [I 05:58:12.260 NotebookApp] http://052316a79947:8888/?token=6d5a18345d3c7cd652ec1bf9be3c5cfa59e6e3cce1ef47ed
    [I 05:58:12.261 NotebookApp]  or http://127.0.0.1:8888/?token=6d5a18345d3c7cd652ec1bf9be3c5cfa59e6e3cce1ef47ed
    [I 05:58:12.261 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 05:58:12.266 NotebookApp]

        To access the notebook, open this file in a browser:
            file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
        Or copy and paste one of these URLs:
            http://052316a79947:8888/?token=6d5a18345d3c7cd652ec1bf9be3c5cfa59e6e3cce1ef47ed
        or http://127.0.0.1:8888/?token=6d5a18345d3c7cd652ec1bf9be3c5cfa59e6e3cce1ef47ed
    ```

- 토큰번호로 주피터 실행하기
    ```py
    # 세번째 서버에서 접속한다면 ip주소 유의
    # 다음 토큰번호는 매번 바뀌므로 유의
    192.168.0.107:8889/?token=6d5a18345d3c7cd652ec1bf9be3c5cfa59e6e3cce1ef47ed

    ```
### 텐서플로 실행 간편화 하기
- 매번 바뀌는 토큰을 매번 docker logs tf01으로 확인하여서 실행해야함
- 따라서 `jupyter_notebook_config.py`에 암호화된 1234의 번호를 입력 시켜놓고
- 주피터 실행시 1234로 진입하도록 해보자
- 다만, 컨테이너내의 주피터 환경설정 파일은 바로 수정이 안되므로 꺼내어 수정 및 넣기
1. 컨테이너 내에서 패스워드 암호화 번호 확보하기
    ```py
    docker exec -it tf01 bash
    # -it : attach
    
    컨테이너> jupyter notebook --generate-config # 주피터 환경설정파일 생성
    컨테이너> ipython # 암호 만들기
    ln [1]: from notebook.auth import passwd
    ln [2]: passwd()
    Enter password: 1234 # 암호 입력
    Verify password: 1234 # 암호 재입력
    # 입력한 비밀번호의 암호화된 번호 확보
    Out[2]: 'sha1:b2a0b1af916c:081c1b09cc5afb83485dfad82f875e5789141c91'
    In[3]: exit() 
    exit # 도커에서 빠져나오기
    ```
1. 수정을 위해 쥬피터 환경변수 파일을 컨테이너 밖에서 수정
    ```py
    # 컨테이너 내부에 있는 파일을 밖의 우분투의 현재 폴더로 복사함
    # 복사 : cp 복사할경로의_파일 복사될경로의_파일명
    # "."  : 현재경로 즉, /home/user1
    # docker cp tf01:/root/.jupyter/jupyter_notebook_config.py /home/user1 # 동일
    docker cp tf01:/root/.jupyter/jupyter_notebook_config.py .
    
    # 복사해온 파일을 편집함
    # cp한 경로 /home/user1
    # nano ~/jupyter_notebook_config.py # 동일
    nano /home/user1/jupyter_notebook_config.py
    281라인 : c.NotebookApp.password = u'sha1로 시작하는 암호...' # 패스워드 암호화번호
    ```
1. 수정 후 다시 컨테이너로 넣고 구동하기
    ```py
    # 편집한 파일을 다시 컨테이너로 복사함.
    # docker cp 원본파일 복사할파일
    docker cp jupyter_notebook_config.py tf01:/root/.jupyter/jupyter_notebook_config.py

    # 컨테이너 중지
    docker stop tf01

    # 컨테이너 다시 구동
    docker start tf01
    ```

 
## 7.2 도커에서 스파크 실행
- pyspark-notebook을 도커내에서 실행시키기
    ```py
    docker pull jupyter/pyspark-notebook
    docker images
    docker run -it --name spark01 -p 8889:8888 jupyter/pyspark-notebook
    ```
- 192.168.99.100:8889 접속

# 8. Kafka & Zookeeper
- zookeeper위에 설치된 통신 서버
- 토픽 생성한 자에게만 통신가능

## 8.1 설치
```py
# 다운로드
wget https://archive.apache.org/dist/kafka/2.2.0/kafka_2.11-2.2.0.tgz

# 압축풀기
tar -zxvf kafka_2.11-2.2.0.tgz => 압축풀기

# 환경설정
nano ~/.bashrc  
# 마지막줄에 다음 추가
export KAFKA_HOME=/home/user1/kafka_2.11-2.2.0
export PATH=$PATH:$KAFKA_HOME/bin
# 추가 후 적용
$ source ~/.bashrc

# 방화벽열기
sudo ufw allow 2181
sudo ufw allow 9092
```

- 편집하기(확인만)
```py
# limitations under the License.
# the directory where the snapshot is stored.
dataDir=/tmp/zookeeper
# the port at which the clients will connect
clientPort=2181
# disable the per-ip limit on the number of connections since this is a non-production config
maxClientCnxns=0
```

## 8.2 서버
- Zookeeper
    ```py
    # zookeeper 서버 구동 &를 마지막에 붙이면 백그라운드로 구동됨
    ~/kafka_2.11-2.2.0/bin/zookeeper-server-start.sh 
    ~/kafka/config/zookeeper.properties &

    # zookeeper 서버 구동 확인
    jps
    # 16494 QuorumPeerMain


    # [필요 시] zookeeper 서버 중지
    ~/kafka_2.11-2.2.0/bin/zookeeper-server-stop.sh
    ```
- 서버 환경 설정
    ```py
    nano ~/kafka_2.11-2.2.0/config/server.properties
    # 다음을 추가기입
    31 라인 : listeners=PLAINTEXT://0.0.0.0:9092
    36 라인 : advertised.listeners=PLAINTEXT://192.168.0.XXX:9092
    123 라인 : zookeeper.connect=127.0.0.1:2181
    가장마지막라인에 추가 : delete.topic.enable=true

    # kafka 서버 구동
    ~/kafka_2.11-2.2.0/bin/kafka-server-start.sh ~/kafka_2.11-2.2.0/config/server.properties &


    # kafka 서버 구동 확인
    jps
    16494 QuorumPeerMain
    1234 Kafka

    # [필요시] kafka 서버 중지
    ~/kafka_2.11-2.2.0/bin/kafka-server-stop.sh    
    ```

## 8.3 토픽
```py
# 토픽 생성 => testTopic2   => 채널
~/kafka_2.11-2.2.0/bin/kafka-topics.sh --create --zookeeper 127.0.0.1:2181 --replication-factor 1 --partitions 1 --topic testTopic2

# 토픽 확인
~/kafka_2.11-2.2.0/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181

# Producer생성 (송신자)
~/kafka_2.11-2.2.0/bin/kafka-console-producer.sh --broker-list 192.168.0.15:9092 --topic testTopic2

# Consumer생성 (수신자)
~/kafka_2.11-2.2.0/bin/kafka-console-consumer.sh --bootstrap-server 192.168.0.15:9092 --topic testTopic2 --from-beginning

# [필요 시 : 토픽삭제]
~/kafka_2.11-2.2.0/bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --delete --topic testTopic2
```

## 8.4 spark-kafka 라이브러리 다운로드
```py
wget https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.11/2.4.5/spark-sql-kafka-0-10_2.11-2.4.5.jar

wget https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.11.0.0/kafka-clients-0.11.0.0.jar
```

# 9. 여러 우분투 연결
## 9.1 호스트 설정
- 각 우분투 ifconfig로 ip주소 확인
    ```py
    # 각 호스트 이름을 확인한 아이피로 변경
    # 완료후 리부팅
    sudo hostnamectl set-hostname 192.168.0.15
    sudo hostnamectl set-hostname 192.168.0.103
    sudo hostnamectl set-hostname 192.168.0.107
    ```
- 호스트 등록하기
        - SERVER1, SERVER2, SERVER3 에 편집
    ```py
    sudo nano /etc/hosts
    # 젤 위쪽에 추가
    ###########################
    # host register
    192.168.0.15    hadoop1
    192.168.0.103    hadoop2
    192.168.0.107    hadoop3
    ##########################

    # 편집 후 서버에 적용하기
    sudo service networking restart
    ```

## 9.2 환경변수 설정
### source ~/.bashrc
- SERVER1, SERVER2, SERVER3 편집
    ```py
    # 아래쪽에 다음 추가
    nano ~/.bashrc
    #export HADOOP_HOME=/home/user1/hadoop-3.1.3
    #export HADOOP_COMMON_HOME=/home/user1/hadoop-3.1.3
    export HADOOP_MAPRED_HOME=${HADOOP_HOME}    
    export HADOOP_HDFS_HOME=${HADOOP_HOME}      
    export YARN_HOME=${HADOOP_HOME}             
    #export HDFS_NAMENODE_USER="user1"
    #export HDFS_DATANODE_USER="user1"
    #export HDFS_SECONDARYNAMENODE_USER="user1"
    #export YARN_RESOURCEMANAGER_USER="user1"
    #export YARN_NODEMANAGER_USER="user1"
    #export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    #export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/#sbin:$JAVA_HOME/bin
    source ~/.bashrc
    # 적용하기
    ```
### 각 서버 xml 편집
- SERVER1, SERVER2, SERVER3 편집
    ```xml
    nano ~/hadoop-3.1.3/etc/hadoop/core-site.xml
    <!-- 변경할 것 없음 -->
    <configuration>
        <property>
            <name>fs.defaultFS</name>
            <value>hdfs://192.168.0.1:9000</value>
        </property>
    </configuration>

    <!-- ################################################ -->

    nano ~/hadoop-3.1.3/etc/hadoop/hdfs-site.xml
    <configuration>
        <property>
            <name>dfs.namenode.name.dir</name>
            <value>/home/user1/hadoop-3.1.3/data/nameNode</value>
        </property>

        <property>
            <name>dfs.datanode.data.dir</name>
            <value>/home/user1/hadoop-3.1.3/data/dataNode</value>
        </property>

        <property>
            <name>dfs.replication</name>
            <value>3</value> <!-- 데이터 노드 개수만큼 -->
        </property>
    </configuration>

    <!-- ################################################ -->

    nano ~/hadoop-3.1.3/etc/hadoop/mapred-site.xml
    <configuration>
        <property>
            <name>mapreduce.jobtracker.address</name>
            <value>192.168.0.15:54311</value><!--첫번째PC로-->
        </property>

        <property><!-- 다음내용 덮어쓰기 -->
            <name>mapreduce.framework.name</name>
            <value>yarn</value>
        </property>
    </configuration>

    <!-- ################################################ -->

    nano ~/hadoop-3.1.3/etc/hadoop/yarn-site.xml
    <configuration>
        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
        </property>

        <property>
            <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
            <value>org.apache.hadoop.mapred.ShuffleHandler</value>
        </property>

        <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>192.168.0.15</value><!--첫번째PC로-->
        </property>
    </configuration>

    ```

## 9.3 암호없이 접속
- SERVER1 에서 암호없이 접속되는지 확인
    - 192.168.0.1에서 192.168.0.2 으로 암호없이 접속가능해야함.
    - 192.168.0.1에서 192.168.0.3 으로 암호없이 접속가능해야함.
    ```py
    # 1번에서 접속방법
    ssh 192.168.0.103
    ssh 192.168.0.107
    # 접속 확인 후 
    exit
    # 돌아온거 확인
    ifconfig
    ```

## 9.4인증키 없거나 오류시 설정방법
- 
    ```py
    # SERVER1에서 인증키 생성 
    ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    chmod 0600 ~/.ssh/authorized_keys

    # SERVER2, SERVER3에 폴더생성 /home/user1/폴더 아래에 .ssh폴더가 있어야 함
    # 해당 경로가서 확인후 없으면 다음실행
    mkdir ~/.ssh

    # SERVER1에서 인증키 인증하게
    scp ~/.ssh/authorized_keys 192.168.0.2:/home/user1/.ssh/authorized_keys
    scp ~/.ssh/authorized_keys 192.168.0.3:/home/user1/.ssh/authorized_keys

    ```

## 9.5 접속 후

- SERVER1에서만
    ```py 
    sudo ufw allow 54311

    nano ~/hadoop-3.1.3/etc/hadoop/masters
    192.168.0.15

    nano ~/hadoop-3.1.3/etc/hadoop/workers
    192.168.0.15
    192.168.0.103
    192.168.0.107
    ```
- SERVER1, SERVER2, SERVER3에서 수행
    ```py
    rm -rf ~/hadoop-3.1.3/data/nameNode
    rm -rf ~/hadoop-3.1.3/data/dataNode

    mkdir -p ~/hadoop-3.1.3/data/nameNode
    mkdir -p ~/hadoop-3.1.3/data/dataNode

    hdfs namenode -format
    ```

## 9.6 정상구동 확인방법
- SERVER1에서 구동시  SERVER2, SERVER3가 꺼져있어도 자동 구동됨.
    ```py
    start-all.sh

    # SERVER1에서 jps
    29555 Jps
    28804 SecondaryNameNode
    29205 NodeManager
    29031 ResourceManager
    28362 NameNode
    28540 DataNode

    # SERVER2에서 jps
    3394 NodeManager
    3230 DataNode
    3519 Jps

    # SERVER3에서 jps
    3161 DataNode
    3437 Jps
    3325 NodeManager

    # 크롬에서 192.168.0.1:9870 수행했을때 datanode가 3개
    # 하나밖에 안뜰때?
    ```


# 10. 각종 설치
``` py
# 그래프 라이브러리
wget http://dl.bintray.com/spark-packages/maven/graphframes/graphframes/0.7.0-spark2.4-s_2.11/graphframes-0.7.0-spark2.4-s_2.11.jar


```
# 주요 명령어 정리
```py
# Hadoop 구동
start-all.sh
# Spark master 구동
start-master.sh
# Spark slave 구동
start-slave.sh spark://127.0.0.1:7077
# 주피터 실행
jupyter notebook


stop-all.sh
# 강제종료(jps시 나오는 번호입력)
kill xxxx
```
## 세부 명령어 모음
### spark 토픽
```py
# 토픽 생성 => testTopic2   => 채널
~/kafka_2.11-2.2.0/bin/kafka-topics.sh --create --zookeeper 127.0.0.1:2181 --replication-factor 1 --partitions 1 --topic testTopic2

# 토픽 확인
~/kafka_2.11-2.2.0/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181

# Producer생성 (송신자)
~/kafka_2.11-2.2.0/bin/kafka-console-producer.sh --broker-list 192.168.0.15:9092 --topic testTopic2

# Consumer생성 (수신자)
~/kafka_2.11-2.2.0/bin/kafka-console-consumer.sh --bootstrap-server 192.168.0.15:9092 --topic testTopic2 --from-beginning

# [필요 시 : 토픽삭제]
~/kafka_2.11-2.2.0/bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --delete --topic testTopic2
```

### Zookeeper 서버
```py
# zookeeper 서버 구동 &를 마지막에 붙이면 백그라운드로 구동됨
~/kafka_2.11-2.2.0/bin/zookeeper-server-start.sh 
~/kafka/config/zookeeper.properties &

# zookeeper 서버 구동 확인
jps
# 16494 QuorumPeerMain


# [필요 시] zookeeper 서버 중지
~/kafka_2.11-2.2.0/bin/zookeeper-server-stop.sh
```