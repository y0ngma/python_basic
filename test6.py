print(__name__, type(__name__))
# __name__은 2가지 값으로 변경된다
# 이것을 이용해 유기적인 코드를 작성가능(선택적 코드진행)
    # 여기서 실행할경우 다음이 출력됨
    # __main__ <class 'str'> 
    # 다른곳에서 "import test6" 라고 실행할 경우 다음이 출력
    # test6 <class 'str'>