방법론
KDD 
CRISP-DM 
SEMMA

- 데이터 유형을 파악하기 위한 절차

질문|yes인 경우
---|---
의미있는 0의 존재|비율형데이터. 통계적 계산 허용
척도 포인트 사이의 간격이 의미를 지니는가?|구간형데이터. 일반적통계가능. (표준편차)
척도 포인트가 순서를 나타내는가?|순서형 데이터. 특정형태의 비모수적 통계 검정에 국한됨
이산형 범주인가|명목형 데이터. 세는것만 가능(최빈값)

SVC|
의사결정트리|DecisionTreeClassifier
랜덤포레스트|RandomForestClassifier
TermFrequencyInverseDocumentFrequency|tfidf

pipeline|전처리 핏 여러단계 처리
GridSearch|하이퍼파라메터 for문

## 형태소 분석기
- Konlpy
    - 