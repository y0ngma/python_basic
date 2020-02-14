import pandas as pd
import xml.etree.ElementTree as et

doc = et.parse('C:/Repository/python_basic/3pandas/coffee/busan_rtr1.xml')
root = doc.getroot() # header, body
"""
result
    header
        columns 에 접근 후 반복문 돌려서 cols에 담고
        pages
    body
        rows 
            row 에 접근 후 반복문 돌려서 rows에 담기
"""    
cols = ['행번호']
rows = []
for child in root: # in header, body 
    for tmp1 in child.getchildren(): # in columns, pages, rows
        if tmp1.tag == 'columns' :
            print('=====COLUMNS======', len(tmp1.getchildren()) ) 
            for i in range(len(tmp1.getchildren()) ):
                cols.append(tmp1[i].text) # 컬럼 길이만큼 반복문 돌려서 담기
                # print('c',tmp1[i].text)
        elif tmp1.tag == 'rows':
            print('=====ROWS======', len(tmp1.getchildren()) )
            for tmp2 in range(len(tmp1.getchildren()) ):
                row = []
                for j in range(len(tmp1[i].getchildren())):
                    # print(tmp1[i][j].text)
                    row.append(tmp1[i][j].text) # row 길이만큼 반복문
                rows.append(row)    
                # rows.append(tmp2[i].text)
                # print('r',tmp1[i].text)
# print(rows[:5][:])
# print(cols)

df = pd.DataFrame(
    data = rows,
    columns = cols
)

print(df.head())