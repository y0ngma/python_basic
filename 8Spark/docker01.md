## 도커 설치하기 (안되어 있는 경우)
```py
# Docker 설치 이미지 리포지토리 키 가져오기
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 리포지토리 추가하는 부분
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   
sudo apt install -y docker-ce docker-ce-cli containerd.io

# user1를 docker그룹에 추가
sudo usermod -aG docker user1

docker --version
    Docker version 19.03.5, build 633a0ea838
# 재부팅
```


## 도커에서 스파크 실행
1. pyspark-notebook을 도커내에서 실행시키기
    ```py
    docker pull jupyter/pyspark-notebook
    docker images
    docker run -it --name spark01 -p 8889:8888 jupyter/pyspark-notebook
    ```
1. 192.168.99.100:8889 접속

```py
createDataFrame
namenode, datanode 디렉토리 생성 : hdfs-site.xml
완전 분산 모드  => 4대의 서버로
hdfs dfs -ls /abc => 
hdfs chown -R 777 /test => -R의 의미가?


# hive에서 테이블 생성
create table TBL1 (as) select * from TBL2
# 테이블  삭제
DROP
스파크 master 포트7077
# 그래프생성시 필요한 라이브러리
from graphframes import GraphFrame
g = GraphFrame(v1, e1)
# 그래프 노드의 개수 구하는것?
print(g.vertices.count())
# 각 노드의 연결된 에지(관계) 수?
g.degrees.show()     
```

## 우분투에서 도커하둡
```py
sudo apt update -y
sudo apt install git -y
# sudo apt-get install git

git clone https://github.com/bbonnin/docker-hadoop-3.git

# git clone 하면 다음 폴더 생성됨. 이동
cd docker-hadoop-3
```


```py
#-----------------------------------------------------
# Dockerfile의 모든 내용 지우고 아래로 내용으로 변경

FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
ENV HADOOP_HOME /opt/hadoop
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

RUN apt-get update
RUN apt-get install -y --reinstall build-essential
RUN apt-get install -y ssh
RUN apt-get install -y rsync
RUN apt-get install -y vim
RUN apt-get install -y net-tools
RUN apt-get install -y openjdk-8-jdk
RUN apt-get install -y python2.7-dev
RUN apt-get install -y libxml2-dev
RUN apt-get install -y libkrb5-dev
RUN apt-get install -y libffi-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y libldap2-dev
RUN apt-get install -y python-lxml
RUN apt-get install -y libxslt1-dev
RUN apt-get install -y libgmp3-dev
RUN apt-get install -y libsasl2-dev
RUN apt-get install -y libsqlite3-dev  
RUN apt-get install -y libmysqlclient-dev

RUN \
    if [ ! -e /usr/bin/python ]; then ln -s /usr/bin/python2.7 /usr/bin/python; fi

RUN \
    wget https://archive.apache.org/dist/hadoop/core/hadoop-3.1.1/hadoop-3.1.1.tar.gz && \
    tar -xzf hadoop-3.1.1.tar.gz && \
    mv hadoop-3.1.1 $HADOOP_HOME && \
    for user in hadoop hdfs yarn mapred; do \
         useradd -U -M -d /opt/hadoop/ --shell /bin/bash ${user}; \

    done && \
    for user in root hdfs yarn mapred; do \
         usermod -G hadoop ${user}; \
    done && \

    echo "export JAVA_HOME=$JAVA_HOME" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_DATANODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
#    echo "export HDFS_DATANODE_SECURE_USER=hdfs" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_NAMENODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_SECONDARYNAMENODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export YARN_RESOURCEMANAGER_USER=root" >> $HADOOP_HOME/etc/hadoop/yarn-env.sh && \
    echo "export YARN_NODEMANAGER_USER=root" >> $HADOOP_HOME/etc/hadoop/yarn-env.sh && \
    echo "PATH=$PATH:$HADOOP_HOME/bin" >> ~/.bashrc

RUN \
    ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys

ADD *xml $HADOOP_HOME/etc/hadoop/

ADD ssh_config /root/.ssh/config

ADD start-all.sh start-all.sh

EXPOSE 8088 9870 9864 19888 8042 8888

CMD bash start-all.sh
ENV DEBIAN_FRONTEND teletype

# 여기까지 Dockerfile
#-----------------------------------------------------
```


### 도커 이미지 빌드
```py
#  도커경로로 이동 해서 수동으로 이미지 빌드
cd docker-hadoop-3 
docker build --no-cache -t hadoop3 .

# 이미지 확인
docker images

# 컨테이너 생성
docker run --hostname=hadoop3 -p 8088:8088 -p 9870:9870 -p 9864:9864 -p 19888:19888 \
  -p 8042:8042 -p 8888:8888 --name hadoop3 -d hadoop3

# 컨테이너 확인
docker container ls
```


```py
# 컨테이너 내부에서 다운로드
docker exec -it mongodb bash

# wget 설치를 위해 업데이트 선행
apt update
apt install wget

# wget을 하려는 경로로 이동 후, 실행
cd /home # 필요시=> mv 파일명 /home 

wget https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.11/2.4.1/mongo-spark-connector_2.11-2.4.1.jar

wget https://repo1.maven.org/maven2/org/mongodb/mongo-java-driver/3.9.1/mongo-java-driver-3.9.1.jar

# 완료 후 EXIT로 컨테이너 탈출

# spark01  컨테이너 구동후 주피터 실행
docker start spark01
docker logs spark01
```


connections - connection Editor 에서
    -server : 192.168.99.100 : 32766
변경 후 저장
