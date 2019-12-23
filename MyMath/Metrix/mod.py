# 모듈 내부에는 변수, 함수, 클래쓰 등이 여러개 존재할 수 있다.
# 변수
pi = 3.14
name = '17:30'
# 함수
def add(a, b):
    return a + b
# 크라쓰
class A():
    def __init_(self):
        print('생성')

if __name__ == '__main__':        
    # test
    print('본 모듈의 개발자가 직접 구동시 작동')
    print(add(1,2))
    A()
else:
    # 제 3자가 이 모듈을 가져다가 사용시
    # __name__ ==>파일명 ==> mod
    # 'mod' == '__main__' => False가 되니 else 코드를 타게 된다.
    pass