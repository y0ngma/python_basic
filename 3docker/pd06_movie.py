
import urllib.request as ul
import json, datetime, time
import pandas as pd

def info():
    movieDate=time.strftime('%Y%m%d', time.localtime(time.time()))
    print(movieDate)
    cine=[{}]
    
    for i in range(0, 30):
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=66e652e1d2656b42f10d93c91e0295e4&targetDt={movieDate}"
        # url = f"http... targetDt={movieDate}" 치환 

        request = ul.Request(url)
        print(request)
        response = ul.urlopen(request)
        print(response)
        rescode = response.getcode()
        print(rescode)
        if (rescode==200):
        responseData = response.read()
        