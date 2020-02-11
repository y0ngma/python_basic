## 입사 팁

- 면접에서 질문이 없는것은 스펙만으로 통과 또는 무관심
- 남들과 다른 포트폴리오에 질문온다

# 데이터 관련 직무

- data scientist
- data engineer
- data analyst

## 데이터 분석 절차

1. 분석 목적 및 방향 결정
   - 인터뷰 및 현황 분석
   - 분석주제 발굴
   - 분석 방향 정의
1. 데이터 선택 및 수집
   - 가설 수립
   - 분석 데이터 정의
   - 분석 데이터 수집
     - 데이터 엔지니어
1. 데이터 탐색 및 정제
   - 샘플링 및 데이터 정제
     - 데이터 엔지니어
   - 파생 변수 생성
   - 데이터 탐색
     - Spark, Python
1. 모델 생성 및 평가
   - 데이터 모델링
   - 결과 해석
   - 모델평가
1. 적용
   - 프로세스 설계
     - 데이터 엔지니어
   - 시스템 개발
     - 데이터 엔지니어
   - 운영적용 및 모니터링(시각화)
     - 데이터 엔지니어

## 시스템화

1. 데이터 수집

   - 원천 데이터 확인
   - 수집 주기 및 방법결정
   - 인프라 결정

kafka
flume
cloud infra

RDB, NoSQL
MapReduce, Spark

## 데이터 엔지니어 주요 역량

- 역량
  1. Java, Scala, python, SQL
  1. DB, Nosql
- 빅테이터 인프라 역량
  1. 분산파일 시스템, 컴퓨팅 등의 기술요소
  1.

## 데이터 사이언티스트

- 시각화 및 보고
- 빅데이터 기술 이해
- R, Python 등 Programming skils
- 통계학 및 기계학습
- Business Knowledge
- 호기심

R, SAS,SPSS, Excel
Hadoop, spark

정형
비정형

## 데이터의 발생

- IoT
  - 숨만 쉬어도 데이터 발생
  - 온도 뿐만 아니라

## 데이터 종류

1. 내부데이터
   - 사내 DB, 기존 연구 데이터
1. 직접 수집한 데이터
   - 실험결과, 설문/리서치 결과
1. 외부데이터
   - 자치구별 데이터
   - 공공데이터
   - kaggle
     - 다양한 데이터를 구할 수 있는 장점
     - 문제해결력을 기르기 위해 스스로 해봐야함
   - SKT big data
   - Amazon AWS datasets
   - UC irvine machine learning repository
   - https://github.com/awesomedata/awesome-public-datasets
1. 내부/외부 데이터 취합하기

## 분석 종류

1. 확증적 분석
   - confirmatory data analysis
   - 미리 설정한 가설을 확인하기 위한 분석
   - 추정과 검정(estimation, test) 등을 활용
1. 탐색적 분석 EDA
   - exploratory data analysis
   - 판다스
   - 변수 관계 등 데이터 자체의 특성을 확인하기 위한 분석
   - 간단한 기술 통계량 계산과 다양한 그래프 활용
   - 모든 데이 분석의 시작단계에서 필수적인 과정
     - 데이터 속에 커피판매량과 관련된 인사이트가 있을까?
1. 요약, 모형
   - aggregation
     - 데이터의 정보를 인식각능한 수준으로 줄이는 과정
     - 그룹별 관측치 수, 평균, 최댓값 계산 등 단순 숫자 요약을 의미
       - "매장 별 혼잡 시간대 계산"
   - model
     - 정해진 알고리즘에 따라 데이턴 속 변수과 관측치 간 관계 확인
     - 가능성을 수치화한 확률로 설명
       - "날씨/요일/시간대에 따른 매장별 손님수와 주문상품 예측"

## 분석 실행

1. 목표
   - 실행 가능성과 활용 가능성을 고려
1. 수집
   - 내부 데이터 및 관련있는 외부 데이터를 활용
1. 탐색적 데이터 분석
   - 변수나 변수 관계에 대한 열린 분석 실행
1. 확증적 데이터 분석/모형 적합
   - 검정, 알고리즘 등을 활용한 분석 실행

## 분석 결과 공유

- 시각화/문서화
- 웹 기반으로 동적 보고서 작성가능
  - R의 Shiny.rstudio.com/gallery

## 머신러닝

| supervised | unsupervised |
| ---------- | ------------ |
| y가 있는것 | y가 없는것   |
| 회귀, 분류 | 군집         |

- 회귀
  - x, y 줄게. x의 숫자 y를 예측해봐
  - continuous Y
    - 연속형 값
    - (스케일이 있는값) 속도, 실수값
    -
- 분류
  - x, y 줄게. x의 y를 분류해봐
  - Discrete Y
    - 이산형값
    - Label로 구분되는값 (스케일이 일정치 않은값)
    - 해충 판별 CCTV
- 군집
  - x줄게. x 를 n개로 나눠봐

* machine learning cheat sheet 참고

| 독립변수              | 종속변수               |
| -------------------- | --------------------- |
| column               | row                   |
| feature              | tuple???              |
| feature vector       | instance              |
| regressor            | regressand            |
| covariabte           | criterion             |
| input variable       | output variable       |
| predictor variable   | response variable     |
| manipulated variable | measured variable     |
| controlled variable  | predicted variable    |
| explanatory variable | explained variable    |
| exposure variable    | experimental variable |
