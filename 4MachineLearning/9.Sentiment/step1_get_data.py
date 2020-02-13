import pandas as pd
import os
import numpy as np
import codecs

def step1_get_data():
    # 데어터 경로
    path = './9.Sentiment/data/aclImdb/'
    # 긍정 도는 부정 의미
    labels = {'pos' :1, 'neg':0}
    # csv 에 저장할 값을 관리할 객체
    df = pd.DataFrame()

    # 디렉토리의 개수만큼 반복한다.
    for s in ('test', 'train'):
        for name in ('pos', 'neg'):
            # 읽어올 파일들이 들어 있는 디렉토리명을 만든다
            subpath = '%s/%s' %(s, name)
            dirpath = path + subpath
            # print(dirpath) 
            # 하면 기존 path에 추가로 하위경로가 붙음

            # 현재 디렉토리안에 있는 파일 목록
            file_list = os.listdir(dirpath)
            # print(file_list)
            # 파일 경로를 for문으로 순회하면서 정보를 가져온다

            for file in file_list:
                fileName = os.path.join(dirpath, file)
                with codecs.open(fileName, 'r', 'utf-8') as fp:
                    txt = fp.read()
                    # print(labels[name], ":", txt)

                # DataFrame 객체에 저장한다
                df = df.append([[txt, labels[name]]], ignore_index=True)
                print(fileName)

    # 컬럼 설정
    df.columns = ['review', 'sentiment']
    #순서를 섞는다
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    # 저장한다
    df.to_csv('./9.Sentiment/data/movie_review.csv', index=False)
