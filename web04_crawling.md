# Crawling

## Table of Content
- Setup
- 데이터별 크롤링 방법
    - json
    - xml
    - csv
    - html 


- Macro    
    - 로그인 정보 넣기 및 클릭 시키기
    - 로그인 이후 페이지
    - 자바스크립트 페이지


## Setup
- Robo 3T (sql 처럼 DB 관리)
    - https://robomongo.org/download
    - Download Robo 3T 최신버전 다운 (압축파일으로. 실행파일은 지저분해지므로)
    - robo3t.exe 실행
        - create 눌러서 다음을 입력한다.
        - address `192.168.99.100` : `32766`

- Beautiful Soup  
    ```bash
    @Anaconda Prompt
    # html에서 정보 가져오기
    conda list beautifulsoup # 설치 확인
    
    conda install beautifulsoup
    conda install pymongo
    conda install bs4
    ```

    
## Macro
- 드라이버를 제공하는 크롬 등을 통해 클릭 자동화등 구현  
파이썬에서 보기 위해 driver 설치  
크롬 도움말-버전확인  
 
