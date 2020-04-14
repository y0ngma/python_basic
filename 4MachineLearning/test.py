from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# %matplotlib inline

X, y = make_classification( n_samples=1000, n_features=4, n_informative=3,
                            n_redundant=0, random_state=42 )
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# max_depth 값의 범위 설정
depth_list = [i for i in range(1, 11)]

# 정확도 저장 리스트 설정
accuracy = []

for max_depth in depth_list:
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    accuracy.append(model.score(X_test, y_test))


# 정확도 시각화
plt.plot(depth_list, accuracy)
plt.xlabel('max_depth')
plt.ylabel('accuracy')
plt.title('accuracy by changing max_depth')
plt.show()

# python_basic\4MachineLearning\Data\bank-additional-full.csv
# C:\Repository\python_basic\4MachineLearning\Data\bank-additional-full.csv

