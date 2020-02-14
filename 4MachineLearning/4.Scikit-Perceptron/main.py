#학습용데이터
from sklearn import datasets
#데이터를 학습용과 테스트용으로 나눌수 있는 함수
from sklearn.model_selection import train_test_split
#데이터 표준화
from sklearn.preprocessing import StandardScaler
#perceptron 머신러닝을 위한 클래스
from sklearn.linear_model import Perceptron
#정확도 게산을 위한 함수
from sklearn.metrics import accuracy_score
#파일 저장을 위해..
import pickle
import numpy as np
#from mylib.plotdregion import *
names=None

def step1_get_data():
    #아이리스 데이터 추출
    iris = datasets.load_iris()
    #print(iris)
    #꽃 정보 데이터 추출
    X= iris.data[:100, [2,3]]#꽃잎 정보
    y=iris.target[:100]      #꽃 종류
    names=iris.target_names[:2]# 꽃 이름
    print(X[0])
    print(y[0])
    print(names[0])
    return X, y

def step2_learnig():
    X, y = step1_get_data()
    # 학습 데이터와 테스트 데이터로 나눈다.
    X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.3, random_state=0) # x트래인에 70개 x테스트에 30개 
    #표준화 작업 : 데이터들을 표준 정규분포로 변환하여
    #적은 학습횟수와 높은 학습 정확도를 갖기 위해 하는 작업
    sc= StandardScaler()
    #데이터를 표준화 한다.
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    #학습한다.
    ml=Perceptron(eta0=0.01, max_iter=40, random_state=0)#같은 숫자를 넣어 같은 랜덤값 생성
    ml.fit(X_train_std,y_train)
    #학습 정확도를 확인해본다.
    X_test_std=sc.transform(X_test)
    y_pred = ml.predict(X_test_std)
    print("학습 정확도 :", accuracy_score(y_test,y_pred))
    #학습이 완료된 객체를 저장한다.
    with open('./4.Scikit-Perceptron/scikit_perceptron.dat', 'wb')as fp :
        pickle.dump(sc, fp)
        pickle.dump(ml, fp)

    print("학습 완료")

def step3_using():
    #학습이 완료된 객체를 복원한다.
    with open('./4.Scikit-Perceptron/scikit_perceptron.dat', 'rb') as fp:
        sc=pickle.load(fp)
        ml=pickle.load(fp)
    while True:
        a1=input("꽃 잎의 너비를 입력해 주세요:")
        a2=input("꽃 잎의 길이를 입력해 주세요:")
        X=np.array([[float(a1), float(a2)]])#위에서 표준화 했으니깐 밑에서도 해야됨
        X_std = sc.transform(X)
        #데이터를 입력해 결과를 가져온다.
        y= ml.predict(X_std)
        #print(y)
        if y[0]==0:
            print('Iris-setosa')
        else :
            print('Iris-versicolor')

            
if __name__ == "__main__":
    step2_learnig()
    step3_using()

