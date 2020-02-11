import numpy as np
import pandas as pd
from perceptron import Perceptron
from time import time
import pickle

def step1_get_data():
    # iris.data에서 읽어온다
    df = pd.read_csv('./iris.data', header=None)
    # print(df)
    # 꽃잎 데이터를 추출한다
    X = df.iloc[0:100, [2, 3]].values
    # print(X)
    # 꽃 종류 데이터를 추출한다
    y = df.iloc[0:100, 4].values

    # 문자열 비교를 위해 where 사용
    # True이면 1, 아니면 -1을 넣는다
    y = np.where(y=='Iris-setosa', 1, -1)
    # print(y)
    return X, y


def step2_learning():
    ppn = Perceptron(eta=0.1)
    data = step1_get_data()
    X = data[0]
    y = data[1]
    # 학습한다
    ppn.fit(X, y)
    print(ppn.errors_)
    print(ppn.w_)
    # 학습이 완료된 객체를 파일로 저장한다.
    with open('./perceptron.dat', 'wb') as fp:
        pickle.dump(ppn, fp)
    print("학습완료")


def step3_using():
    # 파일로 부터 객체를 복원한다.
    with open('./perceptron.dat', 'rb') as fp:
        ppn = pickle.load(fp)

    while True:
        a1 = input("너비를 넣어주세요")
        a2 = input("길이를 넣어주세요")

        X = np.array([float(a1), float(a2)])
        
        # 계산된 결과를 가져온다.
        result = ppn.predict(X)
        if result == 1:
            print("결과 : Iris-setosa")
        else:
            print("결과 : Iris-versicolor")


# step1_get_data()
step2_learning()
step3_using()

# if __name__ == "__main__":
#     step1_learning()
#     step2_using()
