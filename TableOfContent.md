[TOC]
## How-to-Markdown
### footnote
1. 코드블럭
- 다음은 아래와 같이 나온다
```
주피터를 켰을때 시작페이지 바꾸는방법은?[^markdown]
[^markdown]:주피터 시작디렉토리 변경, <https://jackerlab.com/jupyter-notebook-directory-change/> (2020.1.1.)
```
1. 실행된것
주피터를 켰을때 시작페이지 바꾸는방법은?[^markdown]
[^markdown]:주피터 시작디렉토리 변경, <https://jackerlab.com/jupyter-notebook-directory-change/> (2020.1.1.)
#### 출처 제공용 
1. 문장 밖에 각주 번호
    - 온라인 자료
      - 저자, 웹사이트이름(기울임꼴), URL(접속날짜)
      - 예: 레지널드 데일리(Reginald Daily), 시간이 흘러도 변치 않는 위키하우의 예시들, http://www.timelesswikihowexamples.html (2011년 7월 22일 접속)
    - 오프라인 자료
      1. 저서(국내/외국)
        - 글쓴이, 책이름, 출판사, 출판연도, 인용한 쪽 수
        - 이민규, 1%만 바꿔도 인생이 달라진다, 더난 출판, 2007, 123쪽
        - Richard Dawkins, The god delusion, New York, soo7, p51 (외국의 경우 도시 이름)
      1. 번역서
        - 글쓴이, 책이름, 옮긴이, 출판사, 출판연도, 인용쪽수
        - 제인오스틴, 오만과 편견, 윤진관, 전승희 옮김, 민음사, 2007, 321쪽
1. 글 마지막에 참고 문헌 따로 정리
#### 추가 정보 제공용
1. 규칙
  - 설명이 긴 각주는 본문에 넣는다
  - 간략히 쓴다. 
  - 과학분야 저술 시 추가연구 중 기존의 연구결과를 뒤집지 못하는 연구라면 각주에 적는다.

- - - - -
### 수학표현식
이 구문은 $$$sqrt{y-1}$$$ 인라인 방식
아래구문은 블럭으로 표현된다.
$$
MSE = frac{1}{N}\sum\limits_{i=1}^n {y_i - t_i}^2
$$

## ***개발 환경 구축***

### 웹환경구축
- [x] SQL developer
- [x] docker 
- [x] Oracle VM Virtualbox
- [] 

### 파이선 환경 구축
- [x] Anaconda 설치 화면에서 PATH추가하기
- [x] Virtual Studio CODE 설치
- [x] Git 연동하기
- [] 쥬피터 시작경로 D:\python_basic 으로 변경

    학원 자료실 http://192.168.0.119/
#### 1. 개요
 - 파이썬을 기반
 - 데이터 분석(통계적, 시각적), 수집, 전처리등등.
 - 머신러닝, 딥러닝 =>  AI분야(한가지만 잘하는)
   -> nvidia vs amd
   -> nvidia의 cupa가 윈도우와 리눅스 지원(맥은 배제)
 - 빅데이터 처리 => 하둡 클러스터 ~ 시스템,...
 - 파이널 프로젝트

2. 개발 환경
 - OS : window(현재), macos, linux
 - python : 
        - 버전
          - 2.7 <- 맥 기본 설치 버전, 리눅스 기본설치버전
          - 3.x <- 개발 (3.7 or 3.6), 항상 최신버전이 
                     좋은것은 아니다(다른 지원여부 체크) 
        - 설치
          - python.org (파이썬만 깔린다, 가볍다)
            -> 현재 PC에 3.7을 깔았다 => 3.5 필요하다?
                지우고깔아야 한다!!
          - 한 PC에서 여러 버전을 쓸수 있다면
            -> 가상환경을 구축해서 각각 영향을 주지 않고 사용
            -> 이런 요구사항을 간편히 수행할수 있는 
                풀패키지 인스톨러 -> anaconda
            -> https://www.anaconda.com/
            -> 아나콘다의 라이트버전(커맨드 버전)
                miniconda
 - IDE: 개발통합환경
         - 전용툴 :  python IDE(불편), 파이참(무겁다),  
                       파이데브, 스파이더, 
                       jupyter notebook(아주중요)->브라우저코딩
                        L ipython(커맨드스타일 분석툴)+웹(flask)
         - 범용툴 : 기존의 개발환경+ 플러그인 추가
                      vs code + python + anaconda + jupyter
 - 공정관리
         - github.com/ 회원가입 및 대학생이면 인증(차후)
           - 대학생 혜택(private 기능 무료 사용)
         - 개발  PC에 git 설치 
           개발 PC에 git 설치 되어 있어야 함.
           https://git-scm.com/download/win
        모든 폴더를 만들때 readme를 작성 (몇년뒤 기억못하는 나를 위해) 
3. 설치
 - anaconda -> git -> vs code 순으로 
   서로 상관없음
 - 아나콘다 경로
   C:\Users\a\Anaconda3
   Anvanced Options에서 path 체크 할것(주의)

4. vs code 설정
 - 프로젝트를 원하는 위치에 폴더 생성
   - py_projects
   - 해당 폴더를 드레그 해서, vs code에 드롭
   - 해당 위치로 vs code 재오픈
- 에디터 설정
   - File > preferecnces > settings
   - 검색(인덱싱) > 항목 찾아서 수정
      thema > Color Theme > Default Light +
      font > 수치 조정
      전체 줌 ctrl + or ctrl -
      termianl > font 조정(필요하면)
      Theme, font, terminal integrated에서 폰트크기(powershell), 
      전체줌/아웃은 Ctrl +/- 
      리누스 명령어(cmd말고 powershell)을 ctrl `(1옆의 버튼)
   - 왼쪽 메뉴
      - 1 file exploper
      - 2 검색, 대체
      - 3 공정관리:소스 컨트롤
      - 4 디버깅(코드가 오류가 있을때 잡는 방법)
      - 5 플러그인 검색 및 설치
  - 파이썬 설치 한 후에 파이썬 파일 한개를 생성시
      -./python_basic/p1.py
      - vs code가 해당 파일을 인식하고, python경로를 잡거나 
      extention을 설치하라고 유도
      - > vs code 재가동
      - > 좌측메뉴 다섯번째 extention 항목에서 python 검색하여 
        python, python for vscode, python extention pack 설치
    
     
5. git 프로젝트를 관리할 폴더 생성
  - 항상 리프레쉬 해서 꼬이지 않게 습관을 들인다.!!! 중요
  - powershell 에서
    $mkdir py_projects  
    $cd py_projects     
  - git상 프로젝트 다운로드  
    [public]
    $git clone https://github.com/y0ngma/python_basic.git
    [private]
    $git clone https://ID:비번@github.com/y0ngma/python_basic.git
  - vs code에다가 py_projects 폴더를 드래그 앤 드롭   
  - git 사용자 임을 등록(powershell 에서)
      $git config --global user.email "takeit2sy@pusan.ac.kr"  
      $git config --global user.name "y0ngma"  
  5.1 수정내용 업로드(push)
    - 수정내용이 있으면 Ctrl S 로 저장
    - 좌측세번째 공정관리에서 '1일차 수업내용' 등으로 작성하고 'V' 표시를 누른다.
      -이 내용은 깃허브 repository에 제목과 마지막수정시간 사이칸에 표현된다.
    - 좌측하단에 화살표를 눌른다.
  5.2 깃허브 사이트에서(push)
    - 수정하거나 파일을 지울때 Commit 하게 된다.
  5.3 수정내용 다운로드(pull)
    - 

6. Jupyter notebook 설정
  6.1 extension 설치하기
    다음을 cmd 에 입력하여 설치한다.
    conda install -c conda-forge jupyter_nbextensions_configurator
  6.2 jupyter의 Nbextensions탭
    다음을 활성화 한다
    - Collapsible Headings 내용접기
    - Codefolding 코드접기
    - Table of Contents 목차색인
    

