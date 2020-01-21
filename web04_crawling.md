# Crawling

## Table of Content
- Setup
- 서비스를 위한 총 순서
    1. 크롤링
    1. 몽고디비
    1. 몽고디비-오라클로 이동
    1. 오라클에서 번호매기고 중복값,null제거
    1. 장고, json,    등 활용한 서비스 제공


- 데이터별 크롤링 방법
    - json
    - xml
    - csv
    - html 

- Macro    
    - 로그인 정보 넣기 및 클릭 시키기
    - 로그인 이후 페이지
    - 자바스크립트 페이지

---

## css_selector

- 드라이버를 제공하는 크롬 등을 통해 클릭 자동화등 구현  
파이썬에서 보기 위해 driver 설치  
- 크롬 도움말-버전확인-해당버전에 맞는것 다운로드 및 적절경로에 옮기기  

    ```py
    import os

    # 기본 경로에서 상/하위 이동:`BASE_DIR, '../상위' 또는 '하위'`
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('============== base dir============')
    print(os.path.join(BASE_DIR, 'selenium', 'chromedriver.exe'))
    ```

- image 하나 직접 긁어오기
    - 원하는 (사진)우클릭 검사-해당코드우클릭-Copy-css selector  
    `img = driver.find_element_by_css_selector("#image_view_0")`
    
    - 원하는 이미지 검색실행 후 긁어 오기  
    네이버 검색칸에 우클릭 검사<input id="query".. ->copy xpath
        ```py
        from selenium.webdriver.common.keys import Keys
        driver.find_element_by_xpath('//*[@id="query"]').send_key('사과')
        driver.find_element_by_xpath('//*[@id="query"]').send_key(Keys.ENTER)
    
    - 원하는 클래스에 포함되어 <li>안에 감싸인 정보만 가져오기
        ```py
        driver.find_element_by_class_name('rank_top1000_list') \
        .find_elements_by_tag_name("li")
        ```

---


- Beautiful Soup
    - 스크립트 없이 html위주로 렌더링된 페이지 크롤링용

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
---
    
 
