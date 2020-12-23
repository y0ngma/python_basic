## Pandas 시험 정리
```py
sort_values
    # 정렬

np.corrcoef(smoker['분율 (%)'], smoker['num_smoker'])
    # 상관계수
    # 

df.drop(columns=['기관명'], axis=1, inplace=True)
    #

park['면적비율'] = park['면적'].apply(lambda x: np.sqrt(x)*0.01)
    # f = lambda x, y: x + y
    # f(1,4) = 5
s1 = pd.Series([1,2,3], index=['a','b','c'])
s1.map(lambda x: np.sqrt(x)*0.01)

df['columns1'].agg(np.sum)

In [45]: pd.to_datetime(['04-01-2012 10:00'], dayfirst=True)
Out[45]: DatetimeIndex(['2012-01-04 10:00:00'], dtype='datetime64[ns]', freq=None)
```

### 카카오db에서 api로 키워드 검색하기
```py
import requests

KAKAO_API_KEY = '706958df16ad00f2174dc54d1cbac3a8'

url = '''
https://dapi.kakao.com/v2/local/search/keyword.json?
query={0}&category_group_code=PO3
'''.format('서울 중부 경찰서')
headers = {
    'Authorization':'KakaoAK {0}'.format(KAKAO_API_KEY)
}
res = requests.get(url, headers = headers)

print(res) # 200 확인
res = res.json()
print(res['documents'][0]['address_name'],
     res['documents'][0]['y'],
     res['documents'][0]['x'],
     res['documents'][0]['place_name'])
```


### kakao developer 홈피
https://developers.kakao.com/docs/restapi/local
키워드로 검색에서

curl -v -X GET "https://dapi.kakao.com/v2/local/search/keyword.json?y=37.514322572335935&x=127.06283102249932&radius=20000" \
--data-urlencode "query=카카오프렌즈" \
-H "Authorization: KakaoAK 706958df16ad00f2174dc54d1cbac3a8"


kkkk에 나의 앱키를 넣는다

### 한줄로 된 json 포멧을 딕셔너리 깔끔하게 정리하기
vscode 우측하단 -> 클릭 후 json으로 변경
전체 드레그 우클릭 -> Format selection

```json
{
    "meta": {
        "same_name": {
            "region": [],
            "keyword": "카카오프렌즈",
            "selected_region": ""
        },
        "pageable_count": 14,
        "total_count": 14,
        "is_end": true
    },
    "documents": [
        {
            "place_name": "카카오프렌즈 코엑스점",
            "distance": "418",
            "place_url": "http://place.map.kakao.com/26338954",
            "category_name": "가정,생활 > 문구,사무용품 > 디자인문구 > 카카오프렌즈",
            "address_name": "서울 강남구 삼성동 159",
            "road_address_name": "서울 강남구 영동대로 513",
            "id": "26338954",
            "phone": "02-6002-1880",
            "category_group_code": "",
            "category_group_name": "",
            "x": "127.05902969025047",
            "y": "37.51207412593136"
        },
    ...
    ]
}
```
