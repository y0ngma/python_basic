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
주피터를 켰을때 시작페이지 바꾸는방법은? [^markdown]

[^markdown] : 주피터 시작디렉토리 변경, <https://jackerlab.com/jupyter-notebook-directory-change/> (2020.1.1.)
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
- 이 구문은 $sqrt{{y-1}}$ 인라인 방식
- 아래구문은 블럭으로 표현된다.
$$
MSE = frac{1}{N}\sum\limits_{i=1}^n {y_i - t_i}^2
$$


