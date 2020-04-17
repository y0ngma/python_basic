# 크롤링_ 배추
#---

#  크롤링 
from selenium import webdriver   # 웹드라이버 
from selenium.webdriver.common.keys import Keys
import urllib.request

# datetime 
from datetime import datetime
from datetime import timedelta

# 디렉터리 작업용 팩 
import shutil 
import win32com.client  # 이거 파일 확장자 변경시 필요 

#  분석용 툴 
import pandas as pd
# import numpy as np
import time, os

# date_list = [('2019-01-01', '2019-03-31'), ('2019-04-01', '2019-06-30'), ('2019-07-01', '2019-09-30'), ('2019-10-01', '2019-12-31')] 
# print(date_list, len(date_list))
 
# 크롤링 함수 -> 어떤 인자를 받을 것인가? -> 일단은 날짜 
# 시작 년도 , 년도 개수 입력 
def craw_func(year,year_len): # 현재 년도 -> (2015-2020)
    # 크롤링을 할거에요 -> 당연히 드라이버가 필요
    options = webdriver.ChromeOptions()
    
    # 드라이버 옵션  
    # options.add_argument('headless') #화면 표시 X
    options.add_argument("disable-gpu")   
    options.add_argument("lang=ko_KR")    
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36')  # user-agent 

    # 화면에 표시되도록 진행할까요 ?

    date_list = [] 
    for i in range(1, year_len+1):
        print(i)
        # print(year + i)
        print(i,'턴') # 로그
        # year = year # year = year + 1
        # date_list = [(year+'-01-01', year+'-03-31'), (year+'-04-01', year+'-06-30'), (year+'-07-01', year+'-09-30'), (year+'-10-01', year+'-12-31')] 
        date_year = [(str(year)+'-01-01', str(year)+'-03-31'), (str(year)+'-04-01', str(year)+'-06-30'), (str(year)+'-07-01', str(year)+'-09-30'), (str(year)+'-10-01', str(year)+'-12-31')] 
        # print(date_list)
        date_list.append(date_year)

    print(date_list)

    for idx in range(year_len):  
        print(idx)
        for start_date , end_date in date_list[idx]:
            # print('start_date', start_date, 'end_date', end_date)

            order_path = 'https://www.kamis.or.kr/customer/price/wholesale/period.do'
            action_path = f'?action=daily&startday={start_date}&endday={end_date}&countycode=&itemcategorycode={itemcategorycode}&itemcode={itemcode}&kindcode={kindcode}&productrankcode={productrankcode}&convert_kg_yn=N'
            # url 결합  
            url = order_path + action_path
            print(url)

            # 드라이버 가지고 오기 
            driver_path = './driver/chromedriver.exe'  # 드라이버 경로
            driver = webdriver.Chrome(driver_path, options=options )

            # 드라이버를 경로에 전달 

            driver.get(url)
            time.sleep(0.5)

            # 파일 저장 
            Xpath = "/html/body/div[1]/div/div[2]/section[3]/div/a"
            target = driver.find_element_by_xpath(Xpath)
            target.click()
            time.sleep(3)
            driver.close() 

            # 파일 이름 변경 
            Downloads_path = 'C:/Users/admin/Downloads/'
            path = 'C:/Forecast-of-market-price/data/input/'
            name = 'Baechu_wholesale_func'
            os.rename(f'{Downloads_path}가격정보.xls', f'{path}{start_date}_{name}.xls')
            time.sleep(1)

            # xls를 xlsx로 변경(에러때문)
            # 엑셀이 깔려 있어야 진행 가능
            excel = win32com.client.Dispatch("Excel.Application")
            path = path.replace('/','\\')
            # print(path)
            xlwb = excel.Workbooks.Open(f'{path}{start_date}_{name}.xls')
            xlwb.SaveAs(f'{path}{start_date}_{name}.xlsx', FileFormat = 51)
            xlwb.Close()
            excel.Quit()
            time.sleep(1)

            # 파일 삭제

            path = 'C:/Repository/python_basic/4MachineLearning/Data/any' # 오빠경로 
            os.remove(f'{path}{start_date}_{name}.xls')
            time.sleep(0.5)



def to_dataframe():
    # 파일 목록 자동화 처리 하기
    # 데이터 정리하고
    # CSV 파일로 만들기
    pass

# 품목 이름
name = 'Baechu_wholesale_func'

# itemcategorycode : 부류 
# 채소류 : 200, 과일류 : 400
itemcategorycode = 200

# itemcode : 품목
# 무 : 231, 배추 : 211, 사과 : 411, 파 : 246, 배 : 412
itemcode = 211

# kindcode : 품종, 없으면 ''
# 사과-후지 : 05, 배-신고 : 01
kindcode = ''
# productrankcode : 상품 등급
productrankcode = 0


# -------------- # 
# 실행 
craw_func(2015, 1)

# -------------- # 