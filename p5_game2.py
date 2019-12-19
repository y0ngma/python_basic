GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_LEN_MAX  = 9
GAME_LEVEL_LEN_MIN  = 1
IS_DEV_MODE         = True

if not IS_DEV_MODE: #release 버전의 코드가 작동
    # step1
    print( '\n =============\'Enjoy Custom Game world !!\'========== \n ' )
    # step2 
    while True:
        tmp = input(" 게임 제목을 입력하시오,\n \
        단 {}자 이내로 입력 가능합니다.\n ------------------\n=> "\
            .format(GAME_TITLE_LEN_MAX)).strip()
        
        if not tmp: 
            print("------------------\n!!!정확하게 입력하세요!!!")
        elif len(tmp)>GAME_TITLE_LEN_MAX:
            print("------------------\n!!!{}자가 초과되었습니다!!!".\
                format(GAME_TITLE_LEN_MAX)) 
        else:
            game_title = tmp
            print( 'game title', game_title )
            break
    # step3
    while True:
        tmp = input(" player_name을 입력하시오, \n단 {}자 이내로 입력가능\
        \n ------------------\n=>".format(PLAYER_NAME_LEN_MAX)).strip()
        if not tmp:
            print("------------------\n!!!제대로 입력하세요!!!")
        elif len(tmp) <= PLAYER_NAME_LEN_MAX:
            player_name = tmp
            print('player name은 %s' % player_name)
            break
        else:
            print("------------------\n!!!%s자가 초과 되었습니다!!!"%\
                PLAYER_NAME_LEN_MAX)
    # step4
    while True:
        tmp = input(" 게임 난이도를 입력하시오. \n단, %d~%d까지 정수 형태로 \
        제한한다\n ------------------\n =>"\
                % (GAME_LEVEL_LEN_MAX, GAME_LEVEL_LEN_MIN)).strip()
        if not tmp:
            print("------------------\n!!!제대로 입력하세요!!!!")
            continue
        if tmp.isdecimal()==False:
            print("------------------\n!!!정수를 입력하세요!!!")
            continue
        tmp = int(tmp)
        if tmp > GAME_LEVEL_LEN_MAX or tmp <GAME_LEVEL_LEN_MIN:
            print("------------------\n!!!범위안의 레벨을 넣어주세요!!!")
            continue
        game_level = tmp
        break
    print('game level은 %s' % game_level)
else: # test or dev(개발) 버전으로 코드가 작동
    # 매번 입력받아서 테스트하기 시간이 많이 소요되므로, 값을 고정하여 개발
    game_title  ='test game'
    player_name ='guest'
    game_level  = 1
# step5
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
    print('{0:^40}'.format('press any key!!'))
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
# 1. 게임이 시작하면 카드를 섞는다. => 셔플 =>random모듈활용
# 2. 카드를 순서대로 나한장(0), 컴퓨터 한장(1), 나한장(2), 컴퓨터한잔(3)(순서대로 뽑는다)
# 3. 플레이어는 최대 2장 까지 더 받을 수 있다.
#    다시 나 한장(4, 6), 컴터한장(5, 7) -> 최대 2번까지 가능
# 4. 승패=> 내가 가진 카드중 최대값 2개를 합산해서, 특별기능이 있다면 추가계산
#    높은쪽이 승리한다
# 5. 한번에 이기면 (내카드의합-컴터카드합)*100, 카드로 한번 받으면 20점씩 깐다.
# 6. 카드받으면 1.카드를 더 받겠습니까? 아니면 2.승부를 내겠습니까?
# 7. 다시 하시겠습니까? yes => 다시 1번부터 시작, no=>game over!! 종료 실행

ori_card    = [1,2,3,4,5,6,7,8,9,10,'j','q','k','a']
target_card = ori_card[:]
