# 환경변수 또는 게임데이터-> 프로그램에 영향을 미치는 고정값 (임계값) 상수로 빼고
# 향후에는 *.py 바깥쪽으로 빼서 저장(파일 또는 디비 도는 서버)
# 고정값을 바깥으로 뺀다. 문구도 다 빼야함
GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_LEN_MAX  = 9
GAME_LEVEL_LEN_MIN  = 1

    #주석이나 코드 비활성화 하여 간결하게 하는법
    # 절차적 프로그램 실습
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

# step1 게임이 시작하면 "Enjoy Custom Game world"라는 문구를 출력한다
# \의 의미: 후술하는것을 문자열로 변환. 글 안에 '또는 줄바꿈시 앞에 사용
print( '\n =============\'Enjoy Custom Game world !!\'========== \n ' )

# step2 
while True:# 반드시 내부에 break가 있어야 한다
    #   2-1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구 출력
    #       -> 매번 입력을 대기할때 마다 해당 프럼프트 출력하겟다
    # 사용자가 엔터키를 칠때까지 코드를 블럭하고 있다
    # strip으로 양단 공백제거
    tmp = input(" 게임 제목을 입력하시오,\n \
    단 {}자 이내로 입력 가능합니다.\n ------------------\n=> "\
        .format(GAME_TITLE_LEN_MAX)).strip()
    
    if not tmp: #   2-3 아무것도 입력하지 않고 엔터를 치면, 
        # 스페이스바를 몇번치고 엔터를 친것도 같이 처리한다 =
        # 2-3-1 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다
        print("------------------\n!!!정확하게 입력하세요!!!")
    elif len(tmp)>GAME_TITLE_LEN_MAX:#   2-4 20자 이상 입력하면,
        # 2-4-1 "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다  
        print("------------------\n!!!{}자가 초과되었습니다!!!".\
            format(GAME_TITLE_LEN_MAX)) 
    else:#   2-5 20자 이내로 입력하면,
        # 2-5-1 gameTitle라는 변수에 게임 제목을 담고
        game_title = tmp
        #  다음 3 단계로 진입한다 -> 2단계를 끝내라
        break
    # gameTitle이 정의된곳 -> while안 else안에서 정의
    # while 밖에서도 사용이 가능하다?
    # 함수나 클레스 내부에서 정의된 변수가 아닌 변수들은 
    # 모두 전역변수이다.(어느곳에서든지 사용 가능하다)<- variable scope(범위)
print( 'game title', game_title )

#step3
while True:
    tmp = input(" player_name을 입력하시오, \n단 {}자 이내로 입력가능\
    \n ------------------\n=>".format(PLAYER_NAME_LEN_MAX)).strip()
    
    if not tmp:
        print("------------------\n!!!제대로 입력하세요!!!")
    elif len(tmp) <= PLAYER_NAME_LEN_MAX:
        player_name = tmp
        break
    else:
        print("------------------\n!!!%s자가 초과 되었습니다!!!"%\
            PLAYER_NAME_LEN_MAX)
print('player name은 %s' % player_name)

#step4
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
print('game level은 %s' % game_level)

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

############# 긍정상황 스타일
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

#step5
print('-' * 20)
print('현재까지 입력상황')
print('gametitle', game_title)
print('palyer_name', player_name)
print('game_level', game_level)
print('-' * 20)