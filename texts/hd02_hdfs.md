기본명령어|내용
---|---
ls [-d][-h][-R]|디렉토리 목록 보기
cat|/airline/2008.csv|head -5 처음5라인 출력
tail|마지막1KB출력
du [-s][-h]|파일 용량보기
mkdir [-p]|p쓰면 풀경로 다 만들어줌. 안쓰면 현재경로부터 하나씩
put|2008.csv /airline/ 파일 업로드(로컬->HDFS)
get|airline/2008.csv 파일 다운로드(로컬<-HDFS)
cp, mv|파일복사, 이동(HDFS<->HDFS)
rm [-R]|airline/ 디렉토리삭제
rm|2008.csv 파일하나 삭제
count [-p]|카운트값
chmod, chown, chgrp|권한, 소유주, 그룹변경
stat [-R]|통계정보 조회
test|


## 원하는 경로에서 하둡으로 가상폴더 만들기
- http://www.rdatasciencecases.org/Data/Airline/ 에서 2008.csv.bz2 다운
- 압축풀어 놓기

- 가상폴더만들기
    ```powershell
    # 가상폴더 만들기
    dir 
    hdfs dfs -mkdir /airline/
    hdfs dfs -ls / 
    
    # 압축푼 경로로 이동해서 넣기
    hdfs dfs -put .\2008.csv /airline/
    hdfs dfs -ls
    
    ```
    
    - 압축푼 경로에 파일없고
    - 하둡 datanode에 들어있음
    livenode에서|처음값|압축푼후
    ---|---|---
    capacity|237.8 GB| 
    Blocks|0|6
    Block Pool Used|0|662MB(128MB 블럭 6개 쓰므로 다르게 나옴)
    DataloadUsage|0 %|

    
- hadoop jar
  - [읽어들일폴더] [저장할 폴더]
    ```powershell    
    hdfs dfs -put ./speech /
    hadoop jar WordCount.jar /speech/ /output/word_count
    # 100% 하고 끝남
    
    hdfs dfs -ls /output/word_count/part-r-00000
    # 글자수 세기를 application으로 만들어 놓음
    # 
    hdfs dfs -head /output/word_count/part-r-00000
    hdfs dfs -cat /output/word_count/part-r-00000

    hdfs dfs -ls /output/word_count
    # ..../output/wor_count/_SUCCESS
    # ..../output/wor_count/part-r-00000
    ```