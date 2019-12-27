# 모듈 내부에는 변수, 함수, 클래쓰 등이 여러개 존재할 수 있다.
# 변수
pi = 3.14
name = 'Testing import a module'
# 함수
def add(a, b):
    return a + b
def sub(a, b):
    return a - b

# 크라쓰
class A():
    def __init_(self):
        print('클래스 ')

if __name__ == '__main__':        
    # test
    print('안녕하십니까 개발자님')
    print()
else:
    # 제 3자가 이 모듈을 가져다가 사용시
    # __name__ ==>파일명 ==> p7_Module
    # 'p7_Module' == '__main__' => False가 되니 else 코드를 타게 된다.
    print('저희 모듈을 이용해 주셔서 감사합니다.')