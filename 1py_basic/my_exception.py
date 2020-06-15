from UnexpectedRSPValue import BadUserName
from UnexpectedRSPValue import PasswordNotMatched

def sign_up():
    '''회원가입함수'''
    name = "dick"
    password = 123
    print("이름:{} 비밀번호:{}".format(name, password))
    
try:
    print("Sign up")
    sign_up()
    
except BadUserName:
    print("사용할 수 없는 이름입니다.")
except PasswordNotMatched:
    print("비밀번호가 틀립니다.")