
print(__name__, type(__name__))

# 예외 처리
# 코드는 잠재적응로 오류를 가질 수 있다
# 이때, s/w 를 다운되지 않게 하고, 혹윽 그 정보를 수집하고,
# 문제없이 다음단계로 진행시키게 하는 방법

# case1 예외 발생시 코드 진행 확인
print(0)
try:
    print(1)
    print(1/0) # 예외 발생하면 실행안됨
    print(2) # 예외 발생하지 않으면 실행
except Exception as e:
    print(3, e) # 예외 발생하면 대신 실행
else:
    print(4) # 예외 발생하지 않으면 실행
finally:
    print(5) # 예외 상관없이 실행
print(6)