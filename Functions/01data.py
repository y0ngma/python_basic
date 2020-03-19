import numpy as np

def loadData( filename, dir='/content/drive/My Drive/data/ml-100k' ):
  data = list()
  array = list()
  # 파일을 읽어서(한줄씩) => 바로 원하는 형태로 처리
  with open( f'{dir}/{filename}' ) as f:
    # 한줄씩 읽는다
    for line in f:
      # 데이터 추출
      uid, mid, rating, _ = line.split('\t')
      # 데이터를 모양에 맞춰서 추가
      print( type(uid), type(mid) )
      # data.append( {'uid':'1', 'mid':'100'} )
      data.append( {'uid':uid, 'mid':mid} )
      array.append( float(rating) )
      break
      pass
    pass

  return ( data, np.array(array) )

loadData( 'ua.base' ) # ua.test