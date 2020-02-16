import pandas as pd
import xml.etree.ElementTree as et

doc = et.parse('C:/Repository/python_basic/3pandas/coffee/busan_rtr1.xml')
root = doc.getroot() # header, body

row = doc.findall('body/rows/row')

print(type(row))

cnt = 0
for i in row:
    if cnt <10:
        # print(i)
        for tmp_col in i: #각 row의 컬럼에 접근함!
            qq = i.find('uptaeNm') # tag(attrib)로 원하는 elem 접근
            print(qq.text) # 그것의 텍스트 확보
    cnt+=1

# 칼럼으로 포문 돌리면서 -> 아래 예시
li = [5,23,4,65]

for i in li:
    print(i)
# 여기서  '~~~' 부분을 위의 포문을 통해서 각각 넣어준다.
qq = i.find('uptaeNm').text # tag(attrib)로 원하는 elem 접근, text확보

# 리스트, 시리즈나 데이터 프레임에 한 열로 저장시키고

# 만들어 놓은 데이터프레임(병철이형꺼)에 concat을 계속 시켜준다. (반복)

    