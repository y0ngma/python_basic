def loadData( filename, dir='/content/drive/My Drive/data/ml-100k' ):
    data = list()
    array = list()
    # 파일을 읽어서(한줄씩) => 바로 원하는 형태로 처리
    with open( f'{dir}/{filename}' ) as f:
        # 한줄씩 읽는다
        for line in f:
            pass
        pass
    return ( data, np.array(array) )

loadData( 'ua.base' ) # ua.test