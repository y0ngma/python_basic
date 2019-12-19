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

# 전체 룰
# 1. 게임이 시작하면 카드를 섞는다. => 셔플 =>random모듈활용
types   = list('♤◇♡♧')
nums    = list('A23456789')+['10']+list('JQK')
cards       = [i+j for i in types for j in nums ] # 
    # 카드 초기화   
score_table = dict() #
    #점수표 초기화
    # A~K 까지를 키로 보고, 이를 통해 값을 획득하면 간단하게 합산처리
    # 이를 위해 점수 변환표를 준비한다
    # nums[0]~nums[13]에 해당하는 특정문자에 마다
    # nums 자기자신 특정문자값의 인덱스를 리턴한값(0~12에) +1값을 
    # 차례대로 멥핑한것을 dict()에 넣는다.
for key in nums:score_table[key] = nums.index(key)+1 #
    # k = 1 # 이것은 쉬운 버전
    # for key in nums:
    #     score_table[key] = k
    #     k += 1
    # print(score_table)
import random
random.shuffle(cards) #
    # 2. 카드를 순서대로 나한장(0), 컴퓨터 한장(1), 나한장(2), 컴퓨터한잔(3)(순서대로 뽑는다)
print(cards[:8])
print('나의카드', cards[:8:2])
print('컴퓨터의 카드', cards[1:8:2])
my_cards        = cards[:8:2]
my_first_cards  = my_cards[:2]
com_cards       = cards[1:8:2]
com_first_cards = com_cards[:2]

cnt = 0 # 
    #플레그 변수:변수로 흐름을 제어한다 => cnt 카드를 추가로 준 횟수
while True:
    choice = input('1. 카드를 더 받겠습니까? 아니면 2. 승부를 내겠습니까?')
    if choice == '1' and cnt <2:
        cnt += 1
        my_first_cards  = my_cards[:2+cnt]
        com_first_cards = com_cards[:2+cnt] ## 
            # 3. 플레이어는 최대 2장까지 더 받을수 있다
            # 다시 나한장(4,6), 컴퓨터 한장(5,7) -> 최대 2번까지 가능
            # cnt=1인 상태에서
            # my_first_cards = my_cards[:3]
            # com_first_cards= com_cards[:3]
        
    elif choice == '2':
        my_score    = 0
        com_score   = 0 ##
            # 판정을 위해 점수를 획득
            # 4. 승패 => 내가 가진 카드중 최대값 2개를 합산해서, 
            # 특별기능이 있다면 추가 계산해서 높은쪽이 승리한다
            # 5. 한번에 이기면 (내카드의합-컴퓨터카드의합)*100, 
            # 카드르 한번 받으면 20점씩 깐다
        for n in my_first_cards  :my_score  += score_table[ n[1:] ]
        for n in com_first_cards :com_score += score_table[ n[1:] ]

        print('my_score', my_score)
        print('com_score', com_score)
        
        # 6. 카드를 받으면 1. 카드를 더 받겠습니까? 아니면 2. 승부를 내겠습니까?
        # 7. 다시 하시겠습니까? yes => 다시 1번부터 시작, no-> game over!! 종료
        if my_score>com_score:
            print('you win, try again? 1.yes, 2.no')
        if my_score<com_score:
            print('you lose, try again? 1.yes, 2.no')
        else:
            print('Draw! try again? 1. tes, 2. no')
        break
    else:
        print('정확하게 1 or 2를 입력하세요')
        if cnt ==2:
            print('이미 추가 카드를 다 받앗습니다. 2번만 선택할 수 있다')
