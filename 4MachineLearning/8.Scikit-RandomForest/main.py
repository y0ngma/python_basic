#학습용데이터
from sklearn import datasets
#데이터를 학습용과 테스트용으로 나눌수 있는 함수
from sklearn.model_selection import train_test_split
#데이터 표준화
from sklearn.preprocessing import StandardScaler
#perceptron 머신러닝을 위한 클래스
# from sklearn.linear_model import Perceptron
#로지스트 회귀를 위한 클래스
# from sklearn.linear_model import LogisticRegression

#SVM을 위한 클래스
from sklearn.svm import SVC
# 의사결정트리
from sklearn.tree import DecisionTreeClassifier

# 랜덤 포래스트
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

#정확도 게산을 위한 함수
from sklearn.metrics import accuracy_score
#파일 저장을 위해..
import pickle
import numpy as np

# from mylib.plotdregion import *
names=None

def step1_get_data():
    #아이리스 데이터 추출
    iris = datasets.load_iris()
    #print(iris)
    #꽃 정보 데이터 추출
    X= iris.data[:150, [2,3]]#꽃잎 정보
    y=iris.target[:150]      #꽃 종류
    names=iris.target_names[:3]# 꽃 이름
    # print(X[0])
    # print(y[0])
    # print(names[0])
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
        # ml=Perceptron(eta0=0.01, max_iter=40, random_state=0)#같은 숫자를 넣어 같은 랜덤값 생성
        # ml=LogisticRegression(C=1000.0, random_state=0)
        # kernel : 알고리즘 종류, linear, poly, rbf, sigmoid
        # C : 분류의 기준이 되는 경계면을 조절    
        # ml = SVC(kernel = 'linear', C=1.0, random_state=0)
        # criterion : 불순도 측정방식, entropy, gini
        # max_depth : 노드 깊이의 최대값
        # ml = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
    # n_estimators : 포레스트 내의 나무 개수
    # n_jobs : 병렬 처리에서 사용할 코어의 개수
    ml = RandomForestClassifier(criterion='entropy', \
        n_estimators=10, max_depth=3, n_jobs=2, random_state=0)

    ml.fit(X_train_std, y_train)

    #학습 정확도를 확인해본다.
    X_test_std=sc.transform(X_test)
    y_pred = ml.predict(X_test_std)
    print("학습 정확도 :", accuracy_score(y_test,y_pred))

    # 성능확인
    y_true = y_test
    y_hat = ml.predict(X_test_std)
    print("R2 score : ", r2_score(y_true, y_hat))
    print("mean_absolute_error:", mean_absolute_error(y_true, y_hat))
    print("mean_squared_error:", mean_squared_error(y_true, y_hat))
    
    #학습이 완료된 객체를 저장한다.
    with open('./8.Scikit-RandomForest/scikit_perceptron.dat', 'wb')as fp :
        pickle.dump(sc, fp)
        pickle.dump(ml, fp)

    print("학습 완료")

def step2_learnig2():
    X, y = step1_get_data()
    X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.3, random_state=0) # x트래인에 70개 x테스트에 30개 
    sc= StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    ml = DecisionTreeClassifier()
    parameters = {'max_depth':[1,2,3,4,5,6,7], 'min_samples_split':[2,3]}
    grid_ml = GridSearchCV(ml, param_grid=parameters, cv=3, refit=True)
    grid_ml.fit(X_train_std, y_train)
    
    #학습 정확도를 확인해본다.
    print('GridSearchCV 최적 팔라미터:', grid_ml.best_params_)
    print('GridSearchCV 최고정확도: {0:.4f}' .format(grid_ml.best_score_))    
    estimator = grid_ml.best_estimator_
    X_test_std = sc.transform(X_test)
    y_pred = estimator.predict(X_test_std)
    print('테스트 데이터 세트 정확도: {0:.4f}'.format(accuracy_score(y_test, y_pred)))
    #학습이 완료된 객체를 저장한다.
    with open('./7.Scikit-Tree/scikit_perceptron.dat', 'wb')as fp :
        pickle.dump(sc, fp)
        pickle.dump(estimator, fp)

    print("학습 완료")

def step3_using():
    #학습이 완료된 객체를 복원한다.
    with open('./8.Scikit-RandomForest/scikit_perceptron.dat', 'rb') as fp:
        sc=pickle.load(fp)
        ml=pickle.load(fp)
    X=[
        [1.4, 0.2],[1.3,0.2],[1.5,0.2],[4.5,1.5],[4.1,1.0],[4.5,1.5],[5.2,2.0],[5.4, 2.3],[5.1,1.8]

    ]
    X_std=sc.transform(X)
    #결과를 추출한다.
    y_pred=ml.predict(X_std)
    for value in y_pred :
        if value == 0 :
            print('Iris-setosa')
        elif value == 1 :
            print('Iris-versicolor')
        elif value == 2 :
            print('Iris-virginica')

    # while True:
    #     a1=input("꽃 잎의 너비를 입력해 주세요:")
    #     a2=input("꽃 잎의 길이를 입력해 주세요:")
    #     X=np.array([[float(a1), float(a2)]])#위에서 표준화 했으니깐 밑에서도 해야됨
    #     X_std = sc.transform(X)
    #     #데이터를 입력해 결과를 가져온다.
    #     y= ml.predict(X_std)
    #     #print(y)
    #     if y[0]==0:
    #         print('Iris-setosa')
    #     else :
    #         print('Iris-versicolor')

            
if __name__ == "__main__":
    step2_learnig()
    # step2_learnig2()
    step3_using()

# 8