import random #
    # 모듈 가져오기는 가급적 맨위에서 1회만 작성한다
import time 

GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_LEN_MAX  = 9
GAME_LEVEL_LEN_MIN  = 1
IS_DEV_MODE         = True

if not IS_DEV_MODE: #release 버전의 코드가 작동   
    # step1 절차적 프로그램 실습
        # 간단한 게임을 구현하여 
        # 긴 단위의 프로그램을 작성하고, 절차적 프로그램을 이해한다
        # 머드 게임 스타일로 터미널에서 입력하면서 게임을 진행
        # 목적, 파이썬 타입, 연산, 조건, 반복, 흐름제어등을 프로그램을 개발하면서 
        # 심화 학습한다
        # --------------------------------------------------------------------
        # step1 게임이 시작하면 "Enjoy Custom Game world"라는 문구를 출력한다
        # step2 
        #   2-1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구 출력
        #   2-2 사용자가 입력할때가 무제한으로 대기한다 -> 무한루프
        #   2-3 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고
        #       다시 입력 대기한다
        #   2-4 20자 이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력 
        #       대기한다   
        #   2-5 20자 이내로 입력하면 gameTitle라는 변수에 게임 제목을 담고 다음 
        #       3 단계로 진입한다
        # step3
        #   3-1 "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
        #   3-2 입력에 대한 처리는 step2와 동일하다
        #   3-3 플레이어의 이름은 player_name이라는 변수에 담는다
        # step4
        #   4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다"
        #   4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
        #       사용자가 넣을 수 있는 총 케이스를 고려하여 점점 범위가 줄어들게 배치
        #       공백입력, 정수가 될수 없는 값, 1~9이외의 값, 정확하게 넣을 경우
        #       다루는 데이터가 앞2개는 문자열, 뒤2개는 정수형=> 조건문을 나눈다            
        #   4-3 게임 난이도는 game_level 이라는 변수에 담는다
        # ================================================================== 
    print( '\n =============\'Enjoy Custom Game world !!\'========== \n ' ) #
        # \의 의미: 후술하는것을 문자열로 변환. 글 안에 '또는 줄바꿈시 앞에 사용
    # step2 
        # 반드시 내부에 break가 있어야 한다
        #   2-1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구 출력
        #       -> 매번 입력을 대기할때 마다 해당 프럼프트 출력하겟다
        # 사용자가 엔터키를 칠때까지 코드를 블럭하고 있다
        # strip으로 양단 공백제거
    while True:
        tmp = input(" 게임 제목을 입력하시오,\n \
        단 {}자 이내로 입력 가능합니다.\n ------------------\n=> "\
            .format(GAME_TITLE_LEN_MAX)).strip()
        
        if not tmp:  #   
            # 2-3 아무것도 입력하지 않고 엔터를 치면, 
            # 스페이스바를 몇번치고 엔터를 친것도 같이 처리한다 =
            # 2-3-1 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다
            print("------------------\n!!!정확하게 입력하세요!!!")
        elif len(tmp)>GAME_TITLE_LEN_MAX:
            print("------------------\n!!!{}자가 초과되었습니다!!!".\
                format(GAME_TITLE_LEN_MAX)) 
        else:
            game_title = tmp #
                #   2-5 20자 이내로 입력하면,
                # 2-5-1 gameTitle라는 변수에 게임 제목을 담고
                #  다음 3 단계로 진입한다 -> 2단계를 끝내라
            break 
    print( 'game title', game_title ) #
        # gameTitle이 정의된곳 -> while안 else안에서 정의
        # while 밖에서도 사용이 가능하다?
        # 함수나 클레스 내부에서 정의된 변수가 아닌 변수들은 
        # 모두 전역변수이다.(어느곳에서든지 사용 가능하다)<- variable scope(범위)
    # step3
    while True:
        tmp = input(" player_name을 입력하시오, \n단 {}자 이내로 입력가능\
        \n ------------------\n=>".format(PLAYER_NAME_LEN_MAX)).strip()
        if not tmp:
            print("------------------\n!!!제대로 입력하세요!!!")
        elif len(tmp) <= PLAYER_NAME_LEN_MAX:
            player_name = tmp
            myTotalScore = 0 # 초기화. 나의 총 점수
                # 매번게임실행시 0점으로 시작하지 않으려면 저장함수 사용
                # 만약 없으면 0점으로 시작
            break
        else:
            print("------------------\n!!!%s자가 초과 되었습니다!!!"%\
                PLAYER_NAME_LEN_MAX)
    print('player name은 %s' % player_name)
    # step4
    while True: # 내가 짠것 
        #값이 정수일때 %d %d % (값1, 값2)
        tmp = input(" 게임 난이도를 입력하시오.\n 단, %d~%d까지 정수 형태로 제한한다\
            \n ------------------\n =>"\
                % (GAME_LEVEL_LEN_MAX, GAME_LEVEL_LEN_MIN)).strip()
        if not tmp:
            print("------------------\n!!!제대로 입력하세요!!!!")
        elif tmp.isdecimal()==False:
                print("------------------\n!!!정수를 입력하세요!!!")
        else:    
            tmp = int(tmp)
            if tmp > GAME_LEVEL_LEN_MAX or tmp <GAME_LEVEL_LEN_MIN:
                print("------------------\n!!!범위안의 레벨을 넣어주세요!!!")
            else:
                game_level = tmp
                break
    print('game level은 %s' % game_level) #
        ############# C++스타일(부정상황 제외식)
            # while True:
            #     tmp = input(" 게임 난이도를 입력하시오. \n단, %d~%d까지 정수 형태로 \
            # 제한한다\n ------------------\n =>"\
            #             % (GAME_LEVEL_LEN_MAX, GAME_LEVEL_LEN_MIN)).strip()
            #     if not tmp:
            #         print("------------------\n!!!제대로 입력하세요!!!!")
            #         continue
            #     if tmp.isdecimal()==False:
            #         print("------------------\n!!!정수를 입력하세요!!!")
            #         continue
            #     tmp = int(tmp)
            #     if tmp > GAME_LEVEL_LEN_MAX or tmp <GAME_LEVEL_LEN_MIN:
            #         print("------------------\n!!!범위안의 레벨을 넣어주세요!!!")
            #         continue
            #     game_level = tmp
            #     break
            # print('game level은 %s' % game_level)
            ######### 긍정상황 스타일
                # while True:
                #     try: #오류가 발생시 예외처리
                #         tmp = int(input(" 게임 난이도를 입력하시오. \
                #         \n단, %d~%d까지 정수 형태로 제한한다\
                #         \n ------------------\n =>"\
                #         % (GAME_LEVEL_LEN_MAX, GAME_LEVEL_LEN_MIN)).strip())
                #         if 1<= tmp <=9:
                #             game_level = tmp
                #             print('game level은 %s' % game_level)
                #             break
                #         else:
                #             print("------------------\n!!!범위안의 레벨을 넣어주세요!!!")
                #     except Exception as e:
                #         print("------------------\n!!!범위안의 레벨을 넣어주세요!!!")
else: # test or dev(개발) 버전으로 코드가 작동
    # 매번 입력받아서 테스트하기 시간이 많이 소요되므로, 값을 고정하여 개발
    game_title  ='test game'
    player_name ='guest'
    game_level  = 1
    myTotalScore = 0 
# step5
if IS_DEV_MODE:
    print('-' * 20)
    print('현재까지 입력상황')
    print('gametitle', game_title)
    print('palyer_name', player_name)
    print('game_level', game_level)
    print('-' * 20)
# step6
    #인트로(가로길이 40칸. 추후에 해상도로 표현)
    '''
    ========================================
    +       게임제목(중앙정렬)              +
    +           1v 레벨값                  +
    +           "플레이어의 이름"의 연대기  +
    ========================================
                press any key!!             
    '''
    print('='*40)
    print('+{0:^38}+'.format(game_title))
    print('+{0:^38}+'.format('lv : %s' % game_level))
    print('+{0:^34}+'.format('"%s"의 연대기' % player_name))
    print('='*40)
    print('{0:^40}'.format('press enter key!!'))
    while True:input(); break # if/while한줄 쓸때;
# step7
    # 카드 게임
    # 자료구조 설계 연습
    # 트럼프 카드 종류 -> 4가지 타입별 13장 카드 존재.
    # A는 합산값의 *2을 한다. 예: A, 3 => (1+3)*2=8점
    # J=>11, Q=>12, K=-5
    '''
    ♤  : A, 2~10, J, Q, K
    ♡  : A, 2~10, J, Q, K
    ♧  : A, 2~10, J, Q, K
    ◇  : A, 2~10, J, Q, K
    '''
# 전체 룰
types   = list('♤◇♡♧') #
    # 이하는 처음에 한번만 정하면되는 부분. gamecards로 사본을 이용
nums    = list('A23456789')+['10']+list('JQK') #
    #10을 같이 넣거나 list('10')으로 합치면 1,0 따로 분리되므로 
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
score_table['K'] = -5 #
    # 트럼프 K는 패널티를 주어서 -5점이다.
# 1. 매번 시작하면 카드를 셔플 => random모듈활용 -----------------------
isOneGaming = True
while isOneGaming:
    # isOneGaming, myTotalScore가 전역변수임을 알린다
    # ->수정을 가능케 한다.
    
    gamecards = cards[:] # 
        # 원본 카드의 사본
    random.shuffle(gamecards) #
        # 2. 카드를 순서대로 나한장(0), 컴퓨터 한장(1), 나한장(2), 컴퓨터한잔(3)(순서대로 뽑는다)
    print(gamecards[:8])
    print('나의카드', gamecards[:8:2])
    print('컴퓨터의 카드', gamecards[1:8:2])
    my_cards        = gamecards[:8:2]
    my_first_cards  = my_cards[:2]
    com_cards       = gamecards[1:8:2]
    com_first_cards = com_cards[:2]

    cnt = 0 # 
        #플레그 변수:변수로 흐름을 제어한다 => cnt 카드를 추가로 준 횟수
    isGaming = True # 
        #다중while문 안에서 나오고 싶은while문 true 바꾸기 위해
    while isGaming:
        msg = '''
            나의카드 : %s, %s vs 컴의카드 : %s, [HIDEN]
        ''' % (my_first_cards[0], my_first_cards[1], com_first_cards[0])
        print(msg)
        x = 1 
        while True:
            time.sleep(0.5) # 재미로 지연 시간추가(초) 
            print('-'*x)
            x += 1
            if x ==4:break
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

            # 엔터키를 누르면 아래 진행

            # 점수 산출 및 표시
            # myGetScore = (내점수-컴점수)*100 + 카드를 더 받은횟수*(-20)
            # myGetScore = (my)*100 + cnt*(-20)

            
            # 6. 카드를 받으면 1. 카드를 더 받겠습니까? 아니면 2. 승부를 내겠습니까?
            # 7. 다시 하시겠습니까? yes => 다시 1번부터 시작, no-> game over!! 종료
            if my_score > com_score:
                myGetScore = (my_score - com_score)*100 + cnt*(-20) #
                    # 점수 산출 및 표시
                myTotalScore += myGetScore
                print('아~ 이겼네요.. 점수 %s점 획득하였습니다. 현재 총 %s점 입니다.' % (myGetScore,myTotalScore))
                print('you win, try again? 1.yes, 2.no')
            if my_score < com_score: #
                myGetScore = -5 # 지면 5점 뺀다
                myTotalScore += myGetScore
                print('아~ 졌네요..  %s점 잃었습니다. 현재 총 %s점 입니다.' % (myGetScore,myTotalScore))
                print('you lose, try again? 1.yes, 2.no')
            else:
                myGetScore = 0
                print('아~ 비겼네요.. 점수 변동없어요. 현재 총 %s점 입니다.' % (myTotalScore))
                print('Draw! try again? 1. tes, 2. no')
            # 게임저장(함수)
            # 1혹은2를 입력받으면 게임 끝내거나 다시실행
            while True: 
                c_number = input().strip().lower()#
                    # 대소문자 구분없고
                    # 내부적으로 결정 어느쪽으로 처리할지
                if c_number == '1' or c_number == 'y' or c_number == 'yes':
                    isGaming = False
                    break
                elif c_number == '2' or c_number == 'n' or c_number == 'no':
                    isGaming    = False
                    isOneGaming = False
                    break
                else:
                    print('정확하게 1.yes, 2.no 중에 하나를 입력하세요')
        else:
            print('정확하게 1 or 2를 입력하세요')
            if cnt ==2:
                print('이미 추가 카드를 다 받앗습니다. 2번만 선택할 수 있다')
print('bye bye ~ \n GAME OVER')