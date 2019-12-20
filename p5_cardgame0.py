types = list('♠◆♥♣')
nums  = list('A23456789')+['10']+list('JQK')
cards = [ i+j for i in types for j in nums ]
import random
random.seed(1) # 시드 고정:매번 섞는 순서를 고정하게됨
random.shuffle(cards)
print( cards[:8] )
print( '나의 카드', cards[:8:2] )
my_first_card = cards[:8:2][:2]
print( my_first_card )
# -> 정수값 추출:맴버 하나씩추출->슬라이싱or추출or분해 
# 합산값
sum = 0
for n in my_first_card:
    # 타입을 제거(0번째문자)
    tmp = n[1:]
    if tmp == 'A' or tmp == 'J' or tmp == 'Q' or tmp == 'K':
        #-> 합하기
        if   tmp == 'A': sum += 1
        elif tmp == 'J': sum += 11
        elif tmp == 'Q': sum += 12
        elif tmp == 'K': sum += 13
    else:# 기본형이 정수
        #sum += int(tmp)
        #-> 합하기
        sum = sum + int(tmp)
########################################################
# A~k까지를 키로 보고, 이를 통해 값을 획득하면 간단하게 합산처리됨
# 이를 위해 점수 변환표를 준비한다
score_table = dict()
for key in nums:
    # 1 ~ 13값을 차례대로 넣어라
    score_table[ key ] = nums.index( key ) +1
print(score_table)  
# ===============================================
# 합산값
sum = 0
for n in my_first_card:
    sum += score_table[ n[1:] ]
print( '내 최초 카드 2장의 합',  sum)