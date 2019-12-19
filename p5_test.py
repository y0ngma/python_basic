## 정수형 테스터 방법
    # for a in [ '1', '-1', '10','1.1', '0', 'a' ]:
    #     print( a )
    #     print( a.isalnum(), a.isalpha(), a.isascii()  )
    #     print( a.isdecimal(), a.isdigit(), a.isnumeric() )
    #     if a.isnumeric():
    #         print('정수변환', int(a))
    #     print( '-'*20 )

## Random, Shuffle 외부모듈 가져오기
import random
ori_data    = [1,2,3,4,5,6,7,8,9,10,'j','q','k','a']
target_data = ori_data[:] 
# 항상 일정하게 섞이는 값을 원한다=난수가 항상 일정하게 나온다->seed(1)
random.seed()
# 일정한 결과를 내면 => 항상 같은 결과가 나오는 실험환경을 구축가능
# 변수를 바꿔가면서 영향성 등등 분석가능
# 씨드를 고정하지 않으면 => 현재시간이 씨드가 된다.
random.shuffle(target_data) # 섞기 함수
print(ori_data)
print(target_data)

