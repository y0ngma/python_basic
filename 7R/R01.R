
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



#############################################################
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
#############################################################

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
























