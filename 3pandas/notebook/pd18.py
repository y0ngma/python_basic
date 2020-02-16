import pandas as pd
import xml.etree.ElementTree as et

doc = et.parse('C:/Repository/python_basic/3pandas/coffee/busan_rtr1.xml')
root = doc.getroot() # header, body

columns = doc.find('header/columns')
col = []
for child in columns:
    col.append(child.tag)

rows = doc.findall('body/rows/row')
row = []

cnt = 0
for i in rows:
    group=[]
    if cnt <2:
        for tmp1 in i: # 각 row의 컬럼에 접근함!
            elem1 = tmp1.text # tag(attrib)로 원하는 elem 접근
            # print(elem1) # 그것의 텍스트 확보
            group.append(elem1)
        print(group)
        row.append(group)
    cnt+=1
# 칼럼으로 포문 돌리면서 -> 아래 예시

# 여기서  '~~~' 부분을 위의 포문을 통해서 각각 넣어준다.
elem1 = row.find(tmp1).text # tag(attrib)로 원하는 elem 접근, text확보

# 리스트, 시리즈나 데이터 프레임에 한 열로 저장시키고

# 만들어 놓은 데이터프레임에 concat을 계속 시켜준다
    