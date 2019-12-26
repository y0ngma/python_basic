# 특정모듈이 개발한면서 작성한 코드나, 
# 단독 구동시 작동해야 하는 코드는 if __name__ ~ 내부로 처리
# 그외의 것은 밖에 두어도 된다(정의하는 부분)
# 왜냐하면 from_ 수행하면 해당모듈이 메모리에 로드된다
# 경우에 따라서는 코드가 실행될 수도 있으므로, 주의

# test5.py 에서 확인
# from game_nocomment2_func_ending import game_level
from MyMath.Metrix.mod import pi, add