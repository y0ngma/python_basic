## -------------------------------------------------------------------- ##
#warning( library(dplyr) )
#suppressWarnings( library(dplyr) )
library(dplyr)

exam <- read.csv("./Data/csv_exam.csv")
exam

# exam에서 class가 1인 경우만 추출하여 출력
exam %>% filter( class == 1 ) #exam을 filter로 넣고(%>%) 조건문처리
exam %>% filter( class != 1 )
exam %>% filter( class == 1 ) %>% filter(science >= 50)
exam %>% filter( class==1 & science>=50 ) # and.위와 결과 상동
exam %>% filter( math>=90 | english>=90 ) # or
exam %>% filter( math>=90 & english>=90 )

class1 <- exam %>% filter( class==1) # class가 1인 행 추출, class1에 할당
exam %>% filter( class %in% c(1,3,5) ) # 반이 c(1,3,5)에 in인 경우
exam %>% filter( class==1 | class ==3 | class==5 ) # 결과 위와 상동
# %/% 나눗셈의 몫, %% 나눗셈의 나머지

## -------------------------------------------------------------------- ##
# Q1. 자동차 배기량에 따라 고속도로 연비가 다른지 알아보려고 합니다. 
# displ(배기량)이 4 이하인 자동차와 5이상인 자동차 중 어떤 자동차의
# hwy(고속도로 연비)가 평균적으로 더 높은지 알아보세요
# Q2. 제조회사에 따라 연비분석. 아우디와 도요타중 어디가 평균도시연비 높은가?
# Q3. 
mpg <- as.data.frame(ggplot2::mpg)
head(mpg)
target1<- mpg %>% filter( displ <=4 )
target2<- mpg %>% filter( displ >=5 )
mean(target1$hwy)
mean(target2$hwy)
# Q2.
mpg_audi <- mpg %>% filter(manufacturer == "audi" )
mpg_toyota <- mpg %>% filter(manufacturer == "toyota" )
# Q3.
mpg_new <- mpg %>% filter( manufacturer%in% c("chevrolet", "ford", "honda") )
mean(mpg_new$cty)

## -------------------------------------------------------------------- ##

exam %>% select(math, english, class) # 순서 적는데로 가져올수 있음
exam %>% select(-math) # math제외
exam %>% filter( class==1 ) %>% select( english )
exam %>%
  select(id, math) %>%
  head(10)

## -------------------------------------------------------------------- ##

## Q1. mpg데이터는 11개 변수. 이중 일부만 추출해서 분석에 활용.
# class, cty 변수를 추출해 새로운 데이터를 만드세요
# 그의 일부를 출력해서 두 변수로만 구성되었는지 확인
mpg_class_cty <- mpg %>% select(class, cty)
head(mpg_class_cty)
## Q2. 차종에따른 도시연비 비교
# suv와 compact의 어느 차종이 연비 높은지 알아보라. 
mpg_suv <- mpg_class_cty %>% filter(class=='suv')
mpg_compact <- mpg_class_cty %>% filter(class=='compact')
mean(mpg_suv$cty)
mean(mpg_compact$cty)

## -------------------------------------------------------------------- ##

# 정렬 
exam %>% arrange(desc(math))
mpg %>% filter( manufacturer=="audi" ) %>%
  arrange(desc(hwy) ) %>%
  head(5)

# 파생변수
exam %>%
  mutate( total = math+english+science ) %>% 
  head()
exam %>%
  mutate( total = math+english+science ) %>% 
  head() ->
  exam_total
exam_total

exam %>%
  mutate( total = math+english+science,
          mean  = (math+english+science)/3 ) %>%
  head()
# mutate 안에서 ifelse사용가능
exam %>%
  mutate( test = ifelse(science>=60, "pass", "fail") ) %>%
  head

exam %>%
  mutate( total = math+english+science ) %>%
  arrange( desc(total) ) %>%
  head

## -------------------------------------------------------------------- ##
## Q1. mpg의 사본으로 하나의 통합연비 변수 만들어 '합산연비변수'를 추가
mpg %>%
  mutate( (hwy+cty)/2 ) %>%
  head
## Q2. 합산연비변수의 평균?

## Q3. top 3 car data?
mpg %>% arrange( desc(mpg_cty_hwy) )
mpg %>%
  mutate( total = hwy+cty,
          mean  = total/2) %>%
  arrange( desc(mean) ) %>%
  head

## -------------------------------------------------------------------- ##

# summarise
# mutate처럼 컬럼생성해서 group_by별로 계산해준다
exam %>% summarise( mean_math = mean(math) )
exam %>% 
  group_by(class) %>% # 반별로
  summarise( mean_math = mean(math), #평균
             sum_math = sum(math), #합계
             median_math = median(math),# 중앙값
             n = n() ) # 학생수

# sd() # 표준편차
# min() #최소값
# n() # 빈도

mpg %>%
  group_by( manufacturer, drv ) %>%
  summarise( mean_cty = mean(cty) ) %>%
  head(10)

## -------------------------------------------------------------------- ##

## Q1. 회서별 suv의 통합연비편균을 구해 내림차순, 1~5위 출력
mpg %>%
  group_by(manufacturer) %>%
  filter( class == 'suv' ) %>%
  mutate( tot = (cty+hwy)/2) %>%
  summarise( mean_tot = mean(tot) ) %>%
  arrange( desc(mean_tot) ) %>%
  head(5)
## Q2. class별 도시연비를 정렬
mpg %>%
  group_by( class ) %>%
  summarise( mean_cty = mean(cty) ) %>%
  arrange( desc(mean_cty) )
## Q3. 고속도로연비 평균 top3 manufacturer?
mpg %>%
  group_by( manufacturer ) %>%
  summarise( mean_hwy = mean(hwy) ) %>%
  arrange( desc(mean_hwy) ) %>%
  head(3)
## Q4. 경차를 가장 많이 생산하는 회사?
mpg %>%
  group_by( manufacturer ) %>%
  filter( class=="compact" ) %>%
  # 다음과 같이 했을땐 틀림
  #summarise( sum_compact = sum(compact) ) %>%
  #arrange( desc(sum_compact) ) %>% 
  summarise( count = n() ) %>%
  arrange( desc(count) )
mpg %>%
  group_by( manufacturer ) %>%
  summarise( count_compact = n() )
  #arrange( desc(sum_compact) ) %>%

## -------------------------------------------------------------------- ##

# 가로로 합치기
test1 <- data.frame(id = c(1,2,3,4,5),
                    midterm=c(60,80,70,90,85) )
test1
test2 <- data.frame(id = c(1,2,3,4,5),
                    midterm=c(70,83,65,95,80) )
test2
total <- left_join(test1, test2, by='id')
total

# 데이터 활용해 변수추가
# 반별 담인교사 명단 생성
name <- data.frame(class=c(1,2,3,4,5),
                   teacher=c("kim","lee","park","choi","jung") )
name
exam_new <- left_join(exam, name, by="class")
exam_new

# 세로로 합치기
group_a <- data.frame(id = c(1,2,3,4,5),
                    test=c(60,80,70,90,85) )
group_a
group_b <- data.frame(id = c(6,7,8,9,10),
                    test=c(80,70,90,85,60) )
group_b
group_all <- bind_rows(group_a, group_b)
group_all

## -------------------------------------------------------------------- ##

# 다음은 연료이다.
# CNG      = c
# diesel   = d
# ethanol  = e
# preminum = p
# regular  = r
fuel <- data.frame( fl=c("c","d","e","p","r"),
            price_fl = c(2.35, 2.38, 2.11, 2.76, 2.22),
                  stringsAsFactors = F)
fuel
## Q1. mpg데이터에 연료가격변수를 추가하시오
mpg <- as.data.frame(ggplot2::mpg)
mpg <- left_join(mpg, fuel, by="fl")  
mpg
## Q2. model, fl, price_fl변수를 추출해 앞5행 출력
mpg %>%
  select(model, fl, price_fl) %>% head(5)
mpg

## -------------------------------------------------------------------- ##

midwest <- as.data.frame(ggplot2::midwest)
## Q1. 미성년인구백분율을 popadults과 poptotal을 이용해 변수 추가
midwest %>% mutate( ratio_child = (poptotal-popadults)/poptotal*100)-> midwest
#midwest_apt <- midwest %>% mutate((popadults/poptotal)*100)
head(midwest)
## Q2. 미성년인구백분율 5개 지역 출력
midwest %>%
  arrange(desc(ratio_child)) %>%
  select( county, ratio_child ) %>%
  head(5)
## Q3. 분류표 기준에 따라 등급변수 추가 및 각 등급별 몇개지역인가?
# more than 40% = large
# 30~40% = middle
# less than 30% = small
#midwest_apt %>% mutate( test=ifelse(>=40, "large",
#                                    30<=<40, "middle",
#                                    30>, "small") )
midwest <- midwest %>%
  mutate(grade = ifelse( ratio_child>=40, "large",
                   ifelse(ratio_child>=30, "middle", "small")
                        ) 
         )
table(midwest$grade)
## Q4. 아시아인인구백분율인 popasian/total의 하위 10개 지역의 
# state, country, 아시아인인구백분율?
#midwest <- left_join(midwest, (popasian/total)*100, by="")
midwest %>%
  mutate( ratio_asian = (popasian/poptotal)*100 ) %>%
  arrange( ratio_asian ) %>%
  select( state, county, ratio_asian ) %>%
  head(10)

