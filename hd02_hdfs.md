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

    