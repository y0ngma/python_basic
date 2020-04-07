rm(list=ls(all=TRUE)) # 메모리에 로딩되어있는 모든 변수 삭제 

df_midterm <- data.frame(
  english = c(90,80,70,60),
  math = c(90,80,70,60),
  class = c('a','a','b','b') )
write.csv(df_midterm, file = "./Data/df_midterm.csv")

## 성적 데이터셋
df <- read.csv('./Data/csv_exam.csv')
dim(df)
df$mean <- (df$math + df$english + df$science)/3
head(df)

## 차량데이터셋
mpg <- as.data.frame(ggplot2::mpg) # ggplot2의mpg패키지 느낌?
dim(mpg)
tail(mpg)
str(mpg) # 데이터속성 확인
summary(mpg)#'year'의 중앙값과 평균값이 같음. 즉, 편중되지 않았다

install.packages('Rcpp') # 주피터를 관리자권한으로 열어야 설치가능
install.packages('dplyr')
library(dplyr) # dplyr load

df_raw <- data.frame( var1 = c(1,2,1), var2 = c(2,3,2) )
df_raw 
df_new <- df_raw
df_new <- rename(df_new, v2 = var2) # var2를 v2로 수정
df_new

mpg_new <- mpg
mpg_new <- rename(mpg_new, city = cty)
mpg_new <- rename(mpg_new, highway = hwy)
mpg_new$total <- mpg_new$ct 

mpg$test <- ifelse(mpg$total >=20, "pass", "fail")
head(mpg)

table(mpg$test) # 연비 합격 빈도표 생성
library(ggplot2) # ggplot2 로드
qplot(mpg$test) # 연비 합격 빈도 막대그래프 생성

mpg$grade <- ifelse(mpg$total >=30, "A",
                    ifelse(mpg$total >=20, "B", "C")
                    )
head(mpg)
table(mpg$grade) # 등급빈도표 생성
qplot(mpg$grade) # 등급빈도 막대그래프 생성

## 분석실습
### ggplot2패키지에는 미국 동북중부 437개 지역의 인구통계 정보를 
### 담은 데이터가 있습니다
### 문제1. poptotal을 total로, popasian을 asian으로 변수명 변경
### 문제2. total,asian으로 'asian_per_total'만들고 히스토그램
### 문제3. 아시아인구백분율 전체평균구하고 평균 초과/미만에
###        각 'large', 'small'부여하는 파생변수 생성
### 문제4. 'large', 'small'해당지역의 빈도표와 빈도막대그래프생성

rm(list=ls(all=TRUE)) # 메모리에 로딩되어있는 모든 변수 삭제
midwest <- as.data.frame(ggplot2::midwest)
dim(midwest)
head(midwest, 2)
View(midwest)
str(midwest)
summary(midwest)
### 문제1.
library(dplyr) # rename사용시 필요
midwest <- rename(midwest, total=poptotal)
midwest <- rename(midwest, asian=popasian)
### 문제2.
midwest$asian_per_total <- (midwest$asian/midwest$total)*100
hist(midwest$asian_per_total) # ggplot에 포함된것
### 문제3.
midwest$mean <- (mean(midwest$asian_per_total))
midwest$grade <- ifelse(midwest$asian_per_total>midwest$mean, 'large', 'small')
### 문제4.
table(midwest$grade)
qplot(midwest$grade)
