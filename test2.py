types   = list('♤◇♡♧')
nums    = list('A23456789')+['10']+list('JQK')
cards       = [i+j for i in types for j in nums ]
print(types) #변수=리스트('문자열') => ['문', '자', '열']
print(nums)
import random
random.seed()
random.shuffle(cards) 
print(cards[:8])
print('나의카드', cards[:8:2])
my_cards        = cards[:8:2]
my_first_cards  = my_cards[:2]

my_score = 0
for n in my_cards:
    # types을 제거(0번째문자)
    tmp = n[1:] 
    tmp2= n[1:2]
    print(n, tmp, tmp2, 1)
    if tmp=='A' or tmp == 'Q' or tmp=='J' or tmp=='K':
        if    tmp == 'A' : my_score += 1
        elif  tmp == 'J' : my_score += 11
        elif  tmp == 'Q' : my_score += 12
        elif  tmp == 'K' : my_score += 13
    else: #기본형이 정수
        #sum += int(tmp) 아래와 같은 의미
        my_score = my_score + int(tmp)

