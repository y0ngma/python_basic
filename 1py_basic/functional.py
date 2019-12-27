from tensorflow.keras.models import Sequential
model = Sequential()
#model.add(Dense(출력뉴런의 수, 입력뉴런의 수, activation='relu'))
#model.add(Dense(출력뉴런의 수, 이전 층의 출력수, activation='relu'))
#model.add(Dense(출력뉴런의 수, 따라서 생략가능, activation='relu'))
#model.add(Dense(출력층의 뉴런의 개수, 생략가능, activation='relu'))

model.add(Dense(10, input_dim=2, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(60, activation='sigmoid'))

#요약 정리
summary()

#fit() 모델이 오차로부터 매개변수를 업데이트 시키는 과정을 적합화라고 한다.
# 인자순서별 의미:
# 1.훈련데이터
# 2.지도학습에서 레이블데이터
# 3.정수값 에포크.
# 4.배치크기. 기본값은 32, -none가능
# 5.verbose학습중 출력될 문구.0:none,1:진행도막대,2:미니배치마다 손실정보
# 6.validation_data(X-val, y_val) 또는 validation_split=0~1.0 둘중 하나 선택
#     각 에포크마다 검증데이터의 정확도 함께 출력됨. 
#     이 loss값이 높아지기 시작하면 과적합신호.
# 훈련 데이터의 20%를 검증 데이터로 사용.
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0, validation_split=0.2))

# 위의 fit() 코드의 연장선상인 코드
# 첫번째 인자 = 테스트 데이터에 해당됩니다.
# 두번째 인자 = 지도 학습에서 레이블 테스트 데이터에 해당됩니다.
# batch_size = 배치 크기.
model.evaluate(X_test, y_test, batch_size=32)

# predict() : 임의의 입력에 대한 모델의 출력값을 확인합니다.
# 첫번째 인자 = 예측하고자 하는 데이터.
# batch_size = 배치 크기.
model.predict(X_input, batch_size=32)

#save() : 인공 신경망 모델을 hdf5 파일에 저장합니다.
model.save("model_name.h5")
#load_model() : 저장해둔 모델을 불러옵니다.

from tensorflow.keras.models import load_model
model = load_model("model_name.h5")

