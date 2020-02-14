import pandas as pd
import xml.etree.ElementTree as et

def parse_XML(xml_file, df_cols): 
    """Parse the input XML file and store the result in a pandas 
    DataFrame with the given columns. 
    The first element of df_cols is supposed to be the identifier 
    variable, which is an attribute of each node element in the 
    XML data; other features will be parsed from the text content 
    of each sub-element. 
    """
    
    xtree = et.parse(xml_file)
    xroot = xtree.getroot()
    rows = []
    
    for node in xroot: 
        res = []
        res.append(node.attrib.get(df_cols[0]))
        for el in df_cols[1:]: 
            if node is not None and node.find(el) is not None:
                res.append(node.find(el).text)
            else: 
                res.append(None)
        rows.append({df_cols[i]: res[i] 
                     for i, _ in enumerate(df_cols)})
    
    out_df = pd.DataFrame(rows, columns=df_cols)
        
    return out_df
    


# <row>
# <rowNum>1</rowNum>
# <opnSvcNm>휴게음식점</opnSvcNm>
# <opnSvcId>07_24_05_P</opnSvcId>
# <opnSfTeamCode>3310000</opnSfTeamCode>
# <mgtNo>3310000-104-2017-00086</mgtNo>
# <apvPermYmd>20171030</apvPermYmd>
# <apvCancelYmd></apvCancelYmd>
# <trdStateGbn>01</trdStateGbn>
# <trdStateNm>영업/정상</trdStateNm>
# <dtlStateGbn>01</dtlStateGbn>
# <dtlStateNm>영업</dtlStateNm>
# <dcbYmd></dcbYmd>
# <clgStdt></clgStdt>
# <clgEnddt></clgEnddt>
# <ropnYmd></ropnYmd>
# <siteTel>07076202781</siteTel>
# <siteArea>47.20</siteArea>
# <sitePostNo>608020</sitePostNo>
# <siteWhlAddr>부산광역시 남구 대연동 1858번지 대연힐스테이트푸르지오 115동 106-1호</siteWhlAddr>
# <rdnWhlAddr>부산광역시 남구 수영로 345, 115동 1층 106-1호 (대연동, 대연힐스테이트푸르지오)</rdnWhlAddr>
# <rdnPostNo>48432</rdnPostNo>
# <bplcNm>컴포즈커피 대연혁신점</bplcNm>
# <lastModTs>20190719160045</lastModTs>
# <updateGbn>U</updateGbn>
# <updateDt>2019-07-21 02:40:00.0</updateDt>
# <uptaeNm>커피숍</uptaeNm>
# <x>391411.450181345</x>
# <y>184553.672800184</y>
# <sntUptaeNm>커피숍</sntUptaeNm>
# <manEipCnt></manEipCnt>
# <wmEipCnt></wmEipCnt>
# <trdpJubnSeNm></trdpJubnSeNm>
# <lvSeNm></lvSeNm>
# <wtrSplyFacilSeNm>상수도전용</wtrSplyFacilSeNm>
# <totEpNum></totEpNum>
# <hoffEpCnt></hoffEpCnt>
# <fctyOwkEpCnt></fctyOwkEpCnt>
# <fctySilJobEpCnt></fctySilJobEpCnt>
# <fctyPdtJobEpCnt></fctyPdtJobEpCnt>
# <bdngOwnSeNm></bdngOwnSeNm>
# <isreAm></isreAm>
# <monAm></monAm>
# <multUsnUpsoYn>N</multUsnUpsoYn>
# <facilTotScp>47.2</facilTotScp>
# <jtUpsoAsgnNo></jtUpsoAsgnNo>
# <jtUpsoMainEdf></jtUpsoMainEdf>
# <homepage></homepage>
# </row> 

# <columns>
# <opnSvcNm>개방서비스명</opnSvcNm>
# <opnSvcId>개방서비스ID</opnSvcId>
# <opnSfTeamCode>개방자치단체코드</opnSfTeamCode>
# <mgtNo>관리번호</mgtNo>
# <apvPermYmd>인허가일자</apvPermYmd>
# <apvCancelYmd>인허가취소일자</apvCancelYmd>
# <trdStateGbn>영업상태구분코드</trdStateGbn>
# <trdStateNm>영업상태명</trdStateNm>
# <dtlStateGbn>상세영업상태코드</dtlStateGbn>
# <dtlStateNm>상세영업상태명</dtlStateNm>
# <dcbYmd>폐업일자</dcbYmd>
# <clgStdt>휴업시작일자</clgStdt>
# <clgEnddt>휴업종료일자</clgEnddt>
# <ropnYmd>재개업일자</ropnYmd>
# <siteTel>소재지전화</siteTel>
# <siteArea>소재지면적</siteArea>
# <sitePostNo>소재지우편번호</sitePostNo>
# <siteWhlAddr>소재지전체주소</siteWhlAddr>
# <rdnWhlAddr>도로명전체주소</rdnWhlAddr>
# <rdnPostNo>도로명우편번호</rdnPostNo>
# <bplcNm>사업장명</bplcNm>
# <lastModTs>최종수정시점</lastModTs>
# <updateGbn>데이터갱신구분</updateGbn>
# <updateDt>데이터갱신일자</updateDt>
# <uptaeNm>업태구분명</uptaeNm>
# <x>좌표정보(X)</x>
# <y>좌표정보(Y)</y>
# <sntUptaeNm>위생업태명</sntUptaeNm>
# <manEipCnt>남성종사자수</manEipCnt>
# <wmEipCnt>여성종사자수</wmEipCnt>
# <trdpJubnSeNm>영업장주변구분명</trdpJubnSeNm>
# <lvSeNm>등급구분명</lvSeNm>
# <wtrSplyFacilSeNm>급수시설구분명</wtrSplyFacilSeNm>
# <totEpNum>총종업원수</totEpNum>
# <hoffEpCnt>본사종업원수</hoffEpCnt>
# <fctyOwkEpCnt>공장사무직종업원수</fctyOwkEpCnt>
# <fctySilJobEpCnt>공장판매직종업원수</fctySilJobEpCnt>
# <fctyPdtJobEpCnt>공장생산직종업원수</fctyPdtJobEpCnt>
# <bdngOwnSeNm>건물소유구분명</bdngOwnSeNm>
# <isreAm>보증액</isreAm>
# <monAm>월세액</monAm>
# <multUsnUpsoYn>다중이용업소여부</multUsnUpsoYn>
# <facilTotScp>시설총규모</facilTotScp>
# <jtUpsoAsgnNo>전통업소지정번호</jtUpsoAsgnNo>
# <jtUpsoMainEdf>전통업소주된음식</jtUpsoMainEdf>
# <homepage>홈페이지</homepage>
# </columns>