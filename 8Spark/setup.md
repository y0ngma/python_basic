## 순서
1. 우분투 2GB 다운로드
1. Virtual Box에서 우분투 설치
1. 우분투 포트 설정
1. MobaXterm에 포트 연결
1. 하둡
1. 스파크 : 실시간, 빅데이터
1. 아나콘다 주피터
1. pyspark

- 우분투 18.04 다운로드
    `https://ubuntu.com/download/desktop/thank-you?version=18.04.4&architecture=amd64`
## - @virtual box
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

## 우분투
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

## MobaXterm 
- `https://mobaxterm.mobatek.net/download-home-edition.html`
- Free download
    - Portable edition v20.2
- 좌측상단 session 클릭
- ssh 클릭
- Remote host에 `@우분투cmd ifconfig로 확인한 주소` 입력

### 서버주소로 이름 변경
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

## 하둡
```py
# @크롬에서 http://apache.tt.co.kr/hadoop/common/hadoop-3.1.3/
# @페이지에서 마지막 hadoop-3.1.3.tar.gz우클릭 링크주소복사
# @MobaXterm 에서
wget 링크주소 붙여넣기 
ls
tar -zxvf hadoop-3.1.3.tar.gz # 압축풀기
ls

nano ~/.bashrc  => 환경설정 파일
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

source ~/.bashrc # 환경변수 변동사항 적용

```
```py
# 1 #######################################################
nano ~/hadoop-3.1.3/etc/hadoop/hadoop-env.sh

54라인 export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 

# 2 ########################################################
nano ~/hadoop-3.1.3/etc/hadoop/core-site.xml

<configuration>
    <property>
        <name>fs.default.name</name>
        <value>hdfs://192.168.0.XXX:9000</value> ### 자신 주소
    </property>
</configuration>

# 3 #######################################################
nano ~/hadoop-3.1.3/etc/hadoop/hdfs-site.xml

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

<configuration>
    <property>
        <name>map.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>

# 5 #######################################################
nano ~/hadoop-3.1.3/etc/hadoop/yarn-site.xml

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
## d
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
- sudo ufw allow 9000
- sudo ufw allow 9870
- sudo ufw allow 9864
- sudo ufw allow 9866

### 접속
- 크롬에서 192.168.0.XXX:9870
- @Utilities텝
    - Browsee the file system 이 파일 저장소
- hdfs dfs -ls  => 없음
- hdfs dfs -mkdir /test1  => 하둡 파일시스템에 폴더 생성 
- hdfs dfs -chmod -R 777 /test1  =>  /test1의 권한을 모든 사용자가 사용할 수 있게
    - R 하위경로에 대한 권한 범위
    - 777 뜻 (모든사용자 모든 권한)
        - 744, 755 많이 씀

비고|주사용자|그룹|일반인
--|--|--|--
권한여부|Read<br>Write<br>Execute|Read<br>-<br>Execute|Read<br>-<br>- 
이진수|111|101|100
십진수|7|5|4

### 실패시
1. 프로세스 중지
    - stop-all.sh
2. jps로 확인
3. 환경설정 다시확인
4. 데이터노드 네임노드의 폴더안의 파일 지우기
    - rm -rf ~/hadoop-3.1.3/data/nameNode
    - rm -rf ~/hadoop-3.1.3/data/dataNode

    - mkdir -p ~/hadoop-3.1.3/data/nameNode
    - mkdir -p ~/hadoop-3.1.3/data/dataNode

1. name노드 포멧
    - hdfs namenode -format

    - start-all.sh

1. jps
    ```py
    7377 NameNode
    8537 Jps
    8042 ResourceManager
    7580 DataNode
    7822 SecondaryNameNode
    8222 NodeManager
    ``` 
***************************************************

## 아나콘다 3
```py
# 설치중에 홈텝에서 주소 더블클릭해서 창하나 더 열기
# 아나콘다 리눅스버전 64비트 다운로드버튼 우클릭 링크주소복사
wget 우클릭 붙여넣기
ls # 다운로드완료 후 확인
bash Anaconda3-2020.02-Linux-x86_64.sh # yes 두번
source ~/.bashrc # "~" = home/사용자
# rm -rf ~/anaconda3 # 아나콘다 삭제하기

jupyter notebook --generate-config #주피터환경설정파일생성

ipython
In [1]: from notebook.auth import passwd
In [2]: passwd()
    Enter password:1234
    Verify password:1234
Out[2]: 'sha1:34bce7558629:ddac31e930a75c661c4b617f3277a15cd03cc120'
In [3]:exit() # 위 비번을 복사해둔다.

nano ~/.jupyter/jupyter_notebook_config.py
# alt + shift + 3 = 행번호 표시
# ctrl + / + 행번호 = 이동
# 다음을 수정 후 ctrl + S 저장
048라인 : c.NotebookApp.allow_origin = '*'  # 외부 접속 허용하기
204라인 : c.NotebookApp.ip = '10.0.2.15'  #아이피 설정
266라인 : c.NotebookApp.notebook_dir = u'/home/user1/jupyter-workspace' #작업경로 설정
272라인 : c.NotebookApp.open_browser = False # 시작 시 서버PC에서 주피터 노트북 창이 열릴 필요 없음
281라인 : c.NotebookApp.password = u'sha1로 시작하는 암호...' #비밀번호 설정
292라인 : c.NotebookApp.port = 8888   #포트 설정
# 저장 후 
sudo ufw allow 8888 # 방화벽 열기
mkdir ~/jupyter-workplace # 폴더생성
jupyter notebook --config ~/.jupyter/jupyter_notebook_config.py # 크롬에서 192.168.0.15:8888 접속 확인



```

## 스파크 : 실시간, 빅데이터

## 아나콘다 주피터

## pyspark