# -*- coding: utf-8 -*-
"""9.Tensorflow기초.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wEL_mJ5hjEDPYLzo8OO107eztPz6mqOq

# 목적

- 텐서플로우 스타일을 익히고 기본사용법을 습득한

# 스타일

1. 데이터가 흘러가는 플로우를 구성
  - 연산의 입력, 출력의 흐름을 설계
  - 파이썬으로 구성
1. 세션으로 처리(Input/Output)
  - 실제 연산을 수행하는 객체
  1. C++작동시킴
  1. 세션을 연다
  1. 데이터를 입력받음
  1. C++에게 연산 시키고
  1. 결과를 파이썬에게 돌려준다
  1. 세션을 닫는다

# 기본틀
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
import tensorflow as tf
tf.__version__

from IPython.display import Image
# 1. 데이터가 흘러가는 플로우 구성
# 연산을 하려면 요소들이 존재
# 상수
hi = tf.constant('====================  Hello Tensorflow !!  ===============')
print(hi)

# 2. 세션을 열고 데이터를 주입, 실행, 결과를 돌려받는다
# 2-1. 세션을 연다
sess = tf.Session()
# 2-2. 데이터를 주입하여 연산(나중에 신경망) => 학습
# 플로우를 실행함수에 넣어서 연산수행
tmp = sess.run(hi)
# 2-3. 실험결과를 돌려받아 출력
# print(tmp) # b'hi tf'
# 2-4. 세션닫기
sess.close()
####################################################
with tf.Session() as sess: # I/O 문은 열고 닫기 두줄 필요하므로 with문 사용
# GPU 사용 설정은 이 저점 혹은 with문 위가 적절
  print( sess.run(hi) )

"""# Tensorflow를 이용한 연산"""

# 1. 플로우를 구성
# 상수를 정의한다
a = tf.constant(123) # Tensor("Const_4:0", shape=(), dtype=int32)
b = tf.constant(500)
# 'Const_4:0' 은 텐서의 이름(미부여시 자동부과)
# 이름은 향후의 플로우를 시각화해서 텐서보드에서 확인할때의 이름으로 사용

# 2. 계산을 정의(연산식 정의. 실제 연산은 미수행)
# 실제연산은 세션이 열리고 데이터주입, 실행시 작동
add_operation = a+b #Tensor("add_1:0", shape=(), dtype=int32)
# 더한다는 형태(계산식만 가진다)
# 3. 실행
with tf.Session() as sess:
  # 실행후 결과를 돌려받는다
  res =  sess.run(add_operation) #623 <class 'numpy.int32'>

"""# 텐서란 ?"""

f_path = '/content/drive/My Drive/data/DL_data_ref/텐서용어.png'
Image(f_path, width='700')

f_path = '/content/drive/My Drive/data/DL_data_ref/8.tensor.jpeg'
Image(f_path, width='700')

"""# 텐서플로우의 기본 항목

- 상수 : Constant
- 변수 : Variable
- 플레이스홀더: Placeholder
- Data Flow graph :
  - 데이터가 흘러가는 관계
"""

# 상수
a = tf.constant( 100, name='a' )#Tensor("a:0", shape=(), dtype=int32)
b = tf.constant( 200, name='b' )
c = tf.constant( 300, name='c' )
# 변수 : 값이 변한다!!, 변수가 가진 값은 변할 수 있다
# 변수의 값은 연산의 결과로 받겠다
v = tf.Variable( 0, name='v' )#<tf.Variable 'v:0' shape=() dtype=int32_ref>
# 연산식
calc_operation = a + b + c #Tensor("add_3:0", shape=(), dtype=int32)
# 데이터 플로우 그래프
# 변수 v에 calc_operation의 계산값을 대입해라
# a, b, c 라는 상수가 더해져서 v에 흘러들어가는 관계를 정의했다
# a, b, c는 데이터이므로 데이터가 흘러가는 관계 : 데이터플로우 그래프
assign_operation = tf.assign( v, calc_operation ) #Tensor("Assign_2:0", shape=(), dtype=int32_ref)
# 2. 실행
with tf.Session() as sess:
  # 최종 그래프가 입력, 수행
  res = sess.run( assign_operation )
  # print( res, type(res) )#600 <class 'numpy.int32'>
  # 세션이 수행되었다면 변수v에 값이 설정되었을 것이다
  res = sess.run(v)

"""# 데이터주입: Placeholder

- 주입할 데이터의 shape을 결정한다
- 플레이스 홀더를 통해서 학습데이터가 흘러들어간다
- 레이어를 통과할때마다 플레이스 홀더를 통해 shape이 결정된다
- 레이어(신경망)을 구성할때 저하는 수치가 실제적으로 반영되는곳
"""

## 고정크기 플레이스 홀더
# 정수값 3개를 받는 플레이스 홀더를 정의해라
a = tf.placeholder( tf.int32, [3] ) #Tensor("Placeholder_1:0", shape=(3,), dtype=int32)
# 상수
b = tf.constant(2) #<tf.Tensor 'Const_16:0' shape=() dtype=int32>
# 데이터플로우그래프
# 벡터 * 스칼라
x_operation = a * b #<tf.Tensor 'mul_9:0' shape=(3,) dtype=int32>
# 연산수행
with tf.Session() as sess:
  # 데이터를 주입하여, 연산을 수행
  # 데이터를 주입 => feed_dict => {key:value}
  res = sess.run( x_operation, feed_dict={a:[1,2,3]} ) # <class 'numpy.ndarray'>

## 가변크기 플레이스홀더
# 데이터가 어떤 크기의 shape으로 들어올지 모르겠다 = None
a = tf.placeholder( tf.int32, [None] )
b = tf.constant(3)
x2_operation = a * b
with tf.Session() as sess:
  res1 = sess.run( x2_operation, feed_dict={a:[1,2,3]} ) #[3 6 9]
  res2 = sess.run( x2_operation, feed_dict={a:[100, 200]} ) #[300 600]

"""# 세션 구동

- Session()
  - 선 설계 => 후 실행
- InteractiveSession()
  - run()없이, eval()을 통해 바로 실행
"""

sess = tf.InteractiveSession()

m1 = tf.constant( [[1., 2.], [3., 4.]] )#<tf.Tensor 'Const_27:0' shape=(2, 2) dtype=float32>
m2 = tf.constant( [[100.], [200.]] ) #<tf.Tensor 'Const_26:0' shape=(2, 1) dtype=float32>
# 행렬의 곱
tf.matmul( m1, m2 ).eval()

"""# 브로드 캐스팅(CNN구현시 다시 다룸)

- +, -, * 등 행렬 연산시 적용
- 연산을 수행하는 행렬간의 차원이 맞지 않은 경우
- 행렬을 자동으로 늘려서(stretch) 연산이 가능하도록 맞춰줌
"""

Image('/content/drive/My Drive/data/DL_data_ref/br1.png', width = '300')

# xW + b 할때 b가 브로드캐스팅되는 원리 묘사
Image('/content/drive/My Drive/data/DL_data_ref/br2.png', width = '300')

Image('/content/drive/My Drive/data/DL_data_ref/br3.png', width = '300')

Image('/content/drive/My Drive/data/DL_data_ref/br4.png', width = '300')

sess = tf.InteractiveSession()

m1 = tf.constant( [[1., 2.],[3., 4.]] )
m2 = tf.constant( [10.] )
(m1+m2).eval()

