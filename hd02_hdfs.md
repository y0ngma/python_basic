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
    - 
    livenode에서|값
    ---|---
    capacity|237.8 GB 
    Blocks|0
    DataloadUsage|0 %
