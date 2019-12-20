## 정수형 테스터 방법
    # for a in [ '1', '-1', '10','1.1', '0', 'a' ]:
    #     print( a )
    #     print( a.isalnum(), a.isalpha(), a.isascii()  )
    #     print( a.isdecimal(), a.isdigit(), a.isnumeric() )
    #     if a.isnumeric():
    #         print('정수변환', int(a))
    #     print( '-'*20 )

## Random, Shuffle 외부모듈 가져오기
    # import random
    # ori_data    = [1,2,3,4,5,6,7,8,9,10,'j','q','k','a']
    # target_data = ori_data[:] 
    # # 항상 일정하게 섞이는 값을 원한다=난수가 항상 일정하게 나온다->seed(1)
    # random.seed()
    # # 일정한 결과를 내면 => 항상 같은 결과가 나오는 실험환경을 구축가능
    # # 변수를 바꿔가면서 영향성 등등 분석가능
    # # 씨드를 고정하지 않으면 => 현재시간이 씨드가 된다.
    # random.shuffle(target_data) # 섞기 함수
    # print(ori_data)
    # print(target_data)

## 트럼프카드 => 타입4개, 타입별13장
    # # 총카드수 13*4 =52. 일렬로 배치하면
    # CARD_TYPE           = 4
    # CARD_PER_TYPE_SIZE  = 13
    # TOTAL_CARD_COUNT    = CARD_TYPE * CARD_PER_TYPE_SIZE
    # # 모든 카드 생성
    # all_cards           = list(range(TOTAL_CARD_COUNT))
    # # 카드 타입의 순서
    # seq                 = list('♤◇♡♧')
    # card_id             = list('A23456789')+['10']+list('JQK')
    # print(seq)
    # # 33는 ♤k 이다
    # target_number = 33
    # print(seq[int(12/CARD_PER_TYPE_SIZE)])
    # print(target_number % CARD_PER_TYPE_SIZE)

