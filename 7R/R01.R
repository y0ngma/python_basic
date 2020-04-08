# 20.04.06 R첫수업 

## 변수명 만들 때 규칙 
### Rstudio에서의 주석은 # 사용 
### - 첫 글자는 알파벳 또는 '.'로 시작해야함 
### - '.'로 시작 시 바로 뒤에는 숫자가 올 수 없으며, 히든(hidden) 변수가 됨 
### 변수 할당 연산자 <-, ->(왼쪽 값을 오른쪽에 할당) , =, <<-, ->>
### 연산자는 파이썬과 거의 동일 

## 변수 조회 
ls() # 현재 메모리에 올라와있는 것들의 리스트를 출력해 줌
ls.str() # 변수의 이름과 구조를 표시 
ls(all.names=TRUE) # hidden 변수도 표시해 줌 
var1<-3
varA<-seq(1,5) # sequence 함수 : 1부터 5까지 
varB<-seq(1,10, by=3) # 1부터 10까지, 3씩 증가
var1
varA
varB

## 변수/ 값 삭제 
rm(var1) # var1 변수 삭제 
rm(list=c('varA', 'varB')) # varA, varB 변수 삭제 
rm(list=ls(all=TRUE)) # 메모리에 로딩되어있는 모든 변수 삭제 



## -------------------------------------------------------------------- ##
## 데이터 프레임 만들기 
english <- c(90, 80, 70, 60)
math <- c(40,60,80, 100)
class <- c('a','a','b','b') 
df_midterm <- data.frame(english, math) # 데이터 프레임 생성 
print(df_midterm)
df_midterm <- data.frame(english, math, class) 
print(df_midterm)

### 실습 1 : data.frame()과 c()를 조합해서 표의 내용을 데이터 프레임으로 만들어 출력해보세요 
### 실습 2 : 실습 1에서 만든 데이터 프레임을 이용해서 과일 가격 평균, 판매량 평균을 구해보세요 

product <- c("사과", "딸기", "수박") 
price <- c(1800, 1500, 3000) 
sale <- c(24, 38, 13) 

df_ <- c(product, price, sale) 
mean(df_$price) 
mean(df_$sale) 

## -------------------------------------------------------------------- ##

var1<-c(1,2,5,7,8) # 하나의 변수에 여러 값 대입 
var2<-c(1:5) # 1부터 5까지 1씩 증가되는 형태로 데이터 임의 생성 
var1+2 # var1 : 1 3 5 7 8 이었는 데, var1의 각각의 값에 2가 더해진 결과가 나옴 3 4 7 9 10 

str3 <- "Hello World!" 
str5 <- c("Hello!", "World", "is", "good!") 
str5+2 # 문자열에 산술연산자 쓰면 에러남

x<-c(1,2,3)
mean(x)
max(x)
min(x)

str5
paste(str5, collapse = ",") # 합쳐주는 작업을 할 때 배열로 되어있는 애들을 ,를 이용해 합침 
paste(str5, collapse = " ") 
?paste # 함수명(?) 앞에 ? 쓰면, 오른쪽 아래 창에서 함수에 대한 설명 볼 수 있음 

## 데이터를 파악할 때 사용하는 함수들

### 함수 / 기능
### head() / 데이터 앞부분 출력
### tail() / 데이터 뒷부분 출력
### View() / 뷰어 창에서 데이터 확인
### dim() / 데이터 차원 출력
### str() / 데이터 속성 출력
### summary() / 요약 통계량 출력


## -------------------------------------------------------------------- ##

## 패키지 설치 install.packages("패키지명") 
install.packages("ggplot2") 
library(ggplot2) # ggplot 패키지 로드 # 주의 사항 : ""쓰면 안됨! 
x<-c("a","a","b","c")
qplot(x) # 그래프 그리기 
qplot(data=mpg, x = hwy) # data에 mpg, x축에 hwy 변수 지정하여 그래프 생성 
# mpg는 r에서 기본적으로 제공되는 데이터 
?qplot # qplot 사용법 참고하기 

## 시험 점수 변수 만들고 출력하기 
score <- c(80,60,70) 
mean_score <- mean(score) # 전체 평균 변수 만들고 출력하기 
print(mean_score) 
# require(패키지명) # library() 함수와 유사, 주로 함수 안에서 사용함 
# detach("package:패키지명", unload=TRUE)  # 패키지를 언로드 하기 위해서 detach()함수를 사용함 


## readxl 패키지 설치 
install.packages("readxl") 
library(readxl) # readxl 패키지 로드 
df_exam <- read_excel("excel_exam.xlsx") 
df_exam 
mean(df_exam$english)
df_exam_novar <- read_excel("exam_novar.xlsx", col_names = F) # 엑셀 파일에 컬럼명이 없을 경우 col_names = F 
print(df_exam_novar) 

df_exam_sheet <- read_excel("excel_exam_sheet.xlsx", sheet=3 ) # 한 파일에 sheet가 여러개 있다면 
print(df_exam_sheet)

df_csv_exam <- read.csv("csv_exam.csv", stringsAsFactors = F) # 문자가 있는 파일을 불러올 때는 stringsAsFactors = F
print(df_csv_exam)


## R 교재 내용 
### 외부 데이터 이용하기

### 엑셀 파일 
library(readxl) # readxl 패키지 로드
df_exam <- read_excel("excel_exam.xlsx") # 엑셀 파일 불러오기

### csv 파일 
df_csv_exam <- read.csv("csv_exam.csv") # csv 파일 불러오기
write.csv(df_midterm, file = ".Data/df_midterm.csv") # csv 파일로 저장하기

### Rda 파일 
load("df_midterm.rda") # Rda 파일 불러오기
save(df_midterm, file = "df_midterm.rda") # Rda 파일로 저장하기 


## -------------------------------------------------------------------- ##


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



















