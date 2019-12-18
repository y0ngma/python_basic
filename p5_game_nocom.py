print( "Enjoy Custom Game world" )
while True:
    tmp = input("게임 제목을 입력하시오,\n \
    단 20자 이내로 입력 가능합니다.\n").strip()
    if not tmp:
        print("정확하게 입력하세요!")
    elif len(tmp)>20:
        print("20자가 초과되었습니다.") 
    else:
        gameTitle = tmp
        break
print( 'gameTitle', gameTitle )

