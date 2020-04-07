

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
write.csv(df_midterm, file = "df_midterm.csv") # csv 파일로 저장하기

### Rda 파일 
load("df_midterm.rda") # Rda 파일 불러오기
save(df_midterm, file = "df_midterm.rda") # Rda 파일로 저장하기 


