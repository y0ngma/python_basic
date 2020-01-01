# format

## 포맷 후 할일 목록
    - 주사용 프로그램이 잘 실행되는것이 우선순위다


### 0. 그래픽카드, 사운드, 인터넷 (데스크탑의 경우)
### 1. 윈도우 설정
    - 1.1 윈도설치시 MS 로그인 및 설정 로드
    - 1.2 일반계정의 비번을 없애서 시작시 로그인 화면 없앤다.
    - 1.3 관리자권한 얻기 
    #- 1.4 window key + R 에서 regedit 실행 후 아래 경로 붙여넣기 하여 이동
    컴퓨터\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
    EnableLUA 더블클릭 후 1값을 0으로 변경. 재부팅
    #- 1.5 관리자계정으로 로그인후 일반계정에 관리자권한 부여 후 관리자계정 없애는 코드 실행

### 1. 주사용 프로그램의 설치 및 최적화
    - 2.1 Anaconda
    - 2.2 Git   
    - 2.3 CV open
    - 2.4 Chrome
        - 확장프로그램 : 뒤로가기, 애드블럭, 삼성인터넷, VPN
    - 2.5 코딩용 글꼴:ubuntu, Hack, D2(한글) 폰트파일을 다음경로에 복붙
        - C:\Windows\Fonts
    - 2.6


### 3. 유틸리티
    - 3.1 우선순위 유틸리티 : 
        - kaspersky free, kaspersky secure connection
        - CC클리너
        - 반디집(압축)
        - 
        - 

    - 3.2 차순위 유틸리티 :
        - 워드엑셀파워포인트 및 한글
        - 꿀뷰
        - 팟플레이어(영어판:광고없음)
            - 메모장-열기- c:/windows/system32/drivers/etc 에서 '모든파일(*.*)'로 'hosts'를 열어서 마지막에 다음을 추가:
            #아래는 팟플레이어 광고제거용임
            127.0.0.1 p1-play.edge4k.com
            127.0.0.1 p2-play.edge4k.com
            127.0.0.1 p1-play.kgslb.com
            127.0.0.1 kyson.ad.daum.net

 다 가능한지 확인 후 백업 및 복원지점 형성         

## priority install (우선순위폴더 설치)
### 개발 환경구축
#### vs code 폰트 설정하기 (설정에 font family 검색)
1. 보통, monospace(고정폭) 지원 영어폰트는 한글폰트가 없다. (d2coding 예외)
2. 그러한 영어폰트-한글폰트 순:영어는 이쁘게 나오고 없는 한글폰트는 다음 인자에서 찾아씀. 
3. '나눔명조 옛한글', hack => 한글글꼴안의 영어폰트는 이쁘지 않지만 사용되어 뒷인자 무시
4. monospace 아닌 영어폰트가 첫째 자리에 오면 안되는 곳도 있다(터미널)
5. 모든 한글글꼴과, 단어사이 공백있는 폰트는 (쌍)따옴표로 감싸준다
6. Generic font family (안전장치역할):
    - 앞에서 지정한 글꼴들이 없을 때 해당 계열의 글꼴등 중에서 사용
        - 웹페이지경우 클라이언트의 PC에 저장된 폰트를 찾아서 사용하게됨
        - 대부분의 컴퓨터에 없는 폰트를 지정하게 되면 방문자들은 그 폰트로 웹문서를 보지 못하고 브라우저가 선택한 글꼴로 보게 됩니다
    - 맨 마지막 인자
        monospace(고정폭) : Courier, MS Courier New, Prestige, Everson Mono …    
        serif(명조 계열) : Times New Roman, Bodoni, Garamond, Minion Web, …
        sans-serif(고딕 계열) : MS Trebuchet, MS Arial, MS Verdana, Univers, …
        cursive(필기체) : Caflisch Script, Adobe Poetica, Sanvito, Ex Ponto
        fantasy(장식체) : Alpha Geometrique, Critter, Cottonwood, FB Reactor, Studz
        가변폭 글꼴 : 굴림(Gulim), 돋움(Dotum), 바탕(Batang), 궁서(Gungsuh)
        고정폭 글꼴 : 굴림체(GulimChe), 돋움체(DotumChe), 바탕체(BatangChe), 궁서체(GungsuhChe)
7. vs code 폰트설정 예시 :
    'ubuntu mono', '나눔바른펜', monospace
    또는 다음과 같이 적어도 결과는 동일
    "ubuntu mono", hack, '나눔바른펜', "나눔명조 옛한글", d2coding, monospace
8. CSS 파일 제작 예시 : 한글폰트는 ['한글명', 영어명] 병기할 것
    font-family: "굴림", Gulim, Arial, sans-serif;

### 잡다한 
    - 32비트 내장 Microsoft Office 제거 및 64 비트 재설치

## window 10 setting
    - 다시 포맷 및 재설치 번거로움 줄이기 위해
        - 모두 설치 후 시스템 이미지 생성
        - 모두 설치 후 복원지점 설정
    
    - Windows 10 - Fast Startup 윈도우 10 빠른시작 끄기
        
        - 1. 
        - 하드웨어 호환성이 안 좋을 경우 윈도우 10 빠른시작 기능을 사용하면 시스템이 불안정해지는 경우가 있다. 그러나 진짜 문제라고 생각하는 건 이 기능을 사용 할 경우 윈도우 업데이트가 제대로 안 되거나 꼬이는 상황이 간혹 발생하는 이유 중에 하나이기도 하다는 점이다. SSD는 체감이 크지 않기에 빠르시작 기능을 끄는 걸 권유
        - 이 기능을 사용 안 하게 사용자가 설정해도 윈도우 10이 메이저 업데이트(예: 윈도우 10 RS1 > RS2 > RS3 )를 하면 기본으로 빠른시작 기능을 사용하는 설정으로 복원된다. 즉 메이저 업데이트의 경우는 Microsoft가 사용자가 이전에 설정했던 거와 상관없이 다시 이 기능을 키는 쪽으로 설정을 초기화하기에 메이저 업데이트 후에는 재설정해주어야 한다.
            1. 단축키 사용 '윈도우 키 +X' (제어판) -> Power Options (전원 옵션) -> 오른쪽 메뉴에서 Additional power settings 선택
            2. 'Choose what the power buttons do (전원 단추 작동 설정)' 클릭
            3. Change settings that are currently unavailable (현재 사용할 수 없는 설정 변경) 선택. * 이걸 클릭해야 옵션을 선택 할 수 있게 활성화 된다
            4. 하단에 Shutdown settings (종료 설정) 에서 Turn on fast startup (recommended) (빠른 시작 켜기(권장)) 체크 해제

    - 탐색기 첫 화면 내PC로 설정, 최근에 사용한 파일, 최근에 사용한 폴더 설정
        - 탐색기 메뉴(menu) -> 보기(View) -> 옵션(Options) -> 폴더 및 검색 옵션 변경(Change folders and search options)

        1. 파일 탐색기 열기 항목에서 바로가기(Quick access)로 설정되어 있다면 내 PC (This PC) 로 변경하면 된다.

        2. 개인정보 보호란에서
        빠른 실행에 최근에 사용된 파일 표시 (Show frequently used files in Quick access)
        빠른 실행에 최근에 사용된 폴더 표시 (Show frequently used folders in Quick access)
        항목들을 체크 해제하면 된다.

    - 백그라운드 앱 끄기
        1. Windows 10 시작 메뉴 -> Settings(설정) 혹은 단축키(윈도우 키 + i) 사용  
        2. Privacy(개인 정보) 선택
        3. Background apps (백그라운드 앱) 에서 불필요하다고 생각하는 백그라운드 앱들을 끈다

    - 윈도우10 시작메뉴 앱 권유 광고 비활성화 그리고 기타설정
        1. Settings(설정) -> Personalization(개인화) -> Start (시작)
        2. "Occasionally show suggestions in Start(때때로 시작 메뉴에 제안 표시)" Off (꺼짐) 설정
        3. 사용한 파일이나 기록을 남기고 싶지 않다면 Show recently opened items in Jump Lists on Start or the taskbar(시작 메뉴의 점프 목록 또는 작업 표시줄에 최근에 사용한 항목 표시) 도 Off (꺼짐) 설정.
        4. Personalization(개인화) -> Lock Screen (잠금화면)
        5. 배경 항목(Background) 옵션에서 Windows Spotlight(윈도우 스포트라이트)를 선택하지 않는다. Picture(사진) 나 Slideshow(슬라이드쇼)를 선택. Windows Spotlight 의 경우 Bing으로 부터 월페이퍼 이미지를 제공받는데 광고가 포함 된다. 사진이나 슬라이드쇼를 선택하면 해당옵션이 나타난다. "Get fun facts, tips, tricks, and more on your lock screen. (잠금 화면에서 재미있는 정보, 팁, 유용한 정보 등을 가져오기)"를 Off (꺼짐)로 설정
        6. Settings(설정) -> System(시스템) -> Notifications & actions(알림 및 작업 )
        7. "Get tips, tricks, and suggestions as you use Windows" Off (꺼짐) 설정
        * 한글 윈도우 10에서는  ‘Windows 에 대한 팁 표시’로 표기하기도 한다. Off 로 설정하면 된다.

        - 출처: https://blogto.tistory.com/621 [odyssey ★ 오디세이]