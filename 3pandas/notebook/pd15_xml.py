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