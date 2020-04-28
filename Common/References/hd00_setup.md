# 하둡
- HADOOP 이란? High-Availablilty Distruibuted Object-Oriented Platform
  - common
  - HDFS
    - 저장
  - MapReduce 
    - 처리

- 하둡 종류
  - 오픈소스 하둡 배포판
    - 설치 어려움
    - MapReduce, HDFS, Common
  - 밴더 배포판
    - 클라우데라, Hortonworks, 맵압MapR 등이 설치가 쉬움
    - 장점 :
      - 신뢰성
      - 지원
      - 완성도
      - 

- 하둡 설정 스크립트
  - conf/masters
    - 세컨더리 네임노드가 동작하는 노드를 명시
  - conf/slaves
    - 데이터노드와 태스크 트래커가 동작하는 노드 명시
  - conf/hadoop-env.sh
    - 하둡의 모든 프로세스에 적용되는 시스템 환경관련 스크립트
  - conf/core-site.xml
    - 분산파일, 맵리듀스 모두 적용 가능
  - conf/hdfs-site.xml
    - 분산파일 설정 스크립트
  - conf/mapred-site.xml
    - 맵리듀스 설정 스크립트

# 하둡명령어
  - 설치 완료되면 준비완료됨.
    ```bash
    # 모든 데몬
    start-all.sh
    stop-all.sh

    # 
    start-dfs.sh
    stop-dfs.sh

    # 
    start-yarn.sh
    stop-yarn.sh
    ```

- 버전2 또는 3 각각의 실행확인 웹주소
  `http://namenode-ip:50070`
  `http://namenode-ip:9870` 
  - Live Nodes의 값 = Datanode 수

- Full Distributed Mode
  ```
  jps
  ssh slave1 jps
  ssh slave2 jps
  ssh slave3 jps
  ...
  ```


# 하둡 setup
1. java JDK 1.8. xxxx 이하 인지 확인
java -version

1. https://hadoop.apache.org/releases.html 에서 3.1.2 binary 다운

1. 하둡 윈도우 실행용 winutils.zip
    - 하둡용으로 컴파일 된것을 먼저 찾고 그 버전에 맞는 하둡을 받는다.
      1. 반디집을 관리자권한으로 실행시킨 후 hadoop-3.1.2_tar.gz 을 `C:\Bigdata`에 푼다.
      2. hadoop-3.1.2_winutils.zip 압축해제 후 나오는 bin 폴더에 하둡실행하는 파일과 각종 설정파일이 있는듯. 이것을  bin이 있는 `C:\Bigdata\hadoop-3.1.2` 덮어쓰기 한다.
    - pyspark 실행
      ```py
      # repl 환경에서 테스트
      # @cmd 
      pyspark
      nums = sc.parallelize([1,2,3,4])
      nums.map(lambda x: x*x).collect()

      # jupyter 진입 전 findspark 설치
      conda install -c conda-forge findspark
      ```

1. 환경변수에서
    - 설정 후 열려있는 cmd 닫거나 윈도우 재시작 
      - JAVA_HOME을 새로만들기
        ```bash
        # JDK (1.8 이하 확인후) 설치경로 잡아주기
        # where java을 cmd/파워셀 등에 입력하면 설치경로가 아닌 실행파일의 경로가 나옴
        C:\Program Files\Java\jdk1.8.0_211
        ```

      - HADOOP_HOME을 새로만들기
        ```bash
        # 설치경로
        C:\Bigdata\hadoop-3.1.2
        ```

      - SPARK_HOME을 새로 만들기
        ```bash
        C:\Bigdata\spark-2.4.5-bin-hadoop2.7
        ```

      - path에 새로만들기
        ```bash
        C:\bigdata\hadoop-3.1.2\bin
        C:\bigdata\hadoop-3.1.2\sbin
        C:\bigdata\spark-2.4.5-bin-hadoop2.7\bin
        C:\bigdata\spark-2.4.5-bin-hadoop2.7\sbin
        # 다음과 같이 java 위치를 위아래로 이동시킴
        C:\Program Files\Java\jdk1.8.0_211\bin
        C:\Program Files (x86)\Common Files\Oracle\Java\javapath
        ```
      - 환경변수 적용 확인
        - `where java` 또는 `set` 에서 바뀐 경로 확인 필수
        - CMD 창 재시작 후 >where yarn
        - Winutils 확인 >where winutils.exe
      - pySpark 설치
        ```bash
        conda install -c conda-forge pyspark
        ```

1. 네트워크설정
   - 윈도우에서 가분산모드시 생략가능. 리눅스에선 쉽게 가능
1. 방화벽설정
   - 윈도우에서 가분산모드시 생략가능. 리눅스에선 쉽게 가능
1. SSH 설정
   - 윈도우에서 가분산모드시 생략가능. 리눅스에선 쉽게 가능




# 여러 컴퓨터 연결
- 다음을 하면 여러 컴퓨터로 가능
- HADOOP 환경변수 설정
  - 설치된 경로로 가서 다음 파일들을 vs code등 편집기로 수정하면 된다. `C:\Bigdata\hadoop-3.1.2\etc\hadoop`
- @rem은 주석이라는 뜻
  ```bash
  # cmd에서 최상위 경로로 이동 후 JDK설치된 경로의 약어 확인
  cd \ 
  dir /x

  ```

1. hadoop-env.cmd
  - 25번째 줄
    - set JAVA_HOME=%JAVA_HOME% 을 다음 중 하나로 바꾼다
    - set JAVA_HOME=%JAVA_HOME=c:\PROGRA~1\Java\jdk1.8.0_211%
    - set JAVA_HOME=%JAVA_HOME=\c:\PROGRA~1\Java\jdk1.8.0_211%
    - set JAVA_HOME=%JAVA_HOME=/c:/PROGRA~1/Java/jdk1.8.0_211%
    - set JAVA_HOME=%JAVA_HOME=c:\Program" "file\Java\jdk1.8.0_211%

  - 90번째 줄
    - set HADOOP_IDENT_STRING=`%USERNAME%`
    - cmd에서 set 쳐서 USERNAME을 찾아 바꾸기
    - set HADOOP_IDENT_STRING=`admin`

  - 92번째 줄에 새로 작성
    ```
    set HADOOP_PREFIX=C:\Bigdata\hadoop-3.1.2
    set HADOOP_CONF_DIR=%HADOOP_PREFIX%\etc\hadoop
    set YARN_CONF_DIR=%HADOOP_CONF_DIR%
    set PATH=%PATH%;%HADOOP_PREFIX%\bin;%HADOOP_PREFIX%\sbin
    ```
  - `hadoop version`을 cmd 에서 확인가능.

1. core-site.xml
  - tmp폴더를 만들고 다음을 추가
    <configuration>
        <property>    
            <name>fs.default.name</name>
            <value>hdfs://0.0.0.0:9000</value>
        </property>
        <property>
            <name>hadoop.tmp.dir</name>
            <value>/c:/Bigdata/hadoop-3.1.2/tmp</value>
        </property>
    </configuration>

  - 만약 안되면 
    - 0.0.0.0:9000 대신 127.0.0.1
    - `C:\Windows\System32\drivers\etc` 에서 보안프로그램 끄고 hosts 다음과 같이 주석해제
      ```py
      # localhost name resolution is handled within DNS itself.
      127.0.0.1       localhost
      #	::1             localhost
      ```

2. hdfs-site.xml
  - 1 번째것은 복사 몇개 할건지 설정.(1번)
  - 3, 4번째것 namenode용 설정이랑 datanode용 설정
  <configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
  <property>
    <name>dfs.permissions</name>
    <value>false</value>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>/c:/Bigdata/hadoop-3.1.2/namenode</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>/c:/Bigdata/hadoop-3.1.2/datanode</value>
  </property>
  </configuration>

3. mapred-site.xml
  - dddd
  <configuration>
    <property>
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
    </property>
    <property>
      <name>mapred.job.tracker</name>
      <value>0.0.0.0:9001</value>
    </property>
  </configuration>

4. yarn-site.xml
  - 리소스 관리
  <configuration>
    <!-- Site specific YARN configuration properties -->
    <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value>
    </property>
    <property>
      <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
      <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
    <property>
      <name>yarn.log-aggregation-enable</name>
      <value>true</value>
    </property>
    <property>
      <name>yarn.nodemanager.pmem-check-enabled</name>
      <value>false</value>
    </property>
    <property>
      <name>yarn.nodemanager.vmem-check-enabled</name>
      <value>false</value>
    </property>
  </configuration>

5. workers
  - 컴퓨터들 목록 등록하는곳
  - local host 만 있는지 확인
  - `ping localhost` cmd에 입력하면
    ```bash
    ::1의 응답: 시간<1ms # 등으로 아무것도 안나오면 정상
    ```
    - `C:\Windows\System32\drivers\etc`의 hosts 에서 다음을 추가하는식으로 등록가능
      ```py
      # localhost name resolution is handled within DNS itself.
      127.0.0.1       localhost
      #	::1             localhost
      
      # 192.168.0.xx datanode1
      ```
  
  - 정보를 저장하는 공간 생성. 중도에 창 닫지말것
    ```bash
    # 관리자 권한으로 cmd 실행
    hdfs namenode -format
    # Storage directory C:..../namenode has been successfully formatted 확인
    
    start-dfs.cmd
    # 창 2개 추가로 뜨고, 자바 스크립트 허용 확인
    # 안되면 sbin 환경변수 및 hadoop-env.cmd 확인
    
    # 기존창에 다음을 입력
    start-yarn.cmd
    jps
    # NodeManager, Jps, NameNode, DataNode, ResourceManager 5줄 출력확인
    ```

