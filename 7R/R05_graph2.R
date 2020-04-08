## -------------------------------------------------------------------- ##

install.packages("foreign")
install.packages("readxl")
library(foreign)
library(dplyr)
library(ggplot2)
library(readxl)

raw_welfare<-read.spss(file='./Data/Koweps_hpc10_2015_beta1.sav',to.data.frame=T)

welfare <- raw_welfare
welfare <- rename(welfare,
                  sex         = h10_g3,
                  birth       = h10_g4,
                  marriage    = h10_g10,
                  religion    = h10_g11,
                  income      = p1002_8aq1,
                  code_job    = h10_eco9,
                  code_region = h10_reg7)
head(welfare)
View(welfare)
dim(welfare)
str(welfare)
summary(welfare)

## Q1. 성별에 따라 월급이 다를까?
# 변수검토 및 이상치 전처리
class(welfare$sex)
table(welfare$sex)
welfare$sex <- ifelse( welfare$sex == 9, NA, welfare$sex )
table( is.na(welfare$sex) )


# 분석위해 성별로 컬럼명 변환
welfare$sex <- ifelse( welfare$sex == 1, "male", "female" )
table(welfare$sex)
qplot(welfare$sex)

class(welfare$income)
summary(welfare$income)
qplot(welfare$income)
qplot(welfare$income) + xlim(0, 1000)

welfare$income <- ifelse( welfare$income %in% c(0, 9999), NA, welfare$income )
table( is.na(welfare$income) )

sex_income <- welfare %>%
  filter( !is.na(income) ) %>%
  group_by(sex) %>%
  summarise( mean_income = mean(income) )
sex_income

ggplot( data =sex_income, aes(x=sex, y=mean_income) ) + geom_col()

## Q2. 나이와 월급의 관계
class(welfare$birth)
summary(welfare$birth)
qplot(welfare$birth)

welfare$birth <- ifelse( welfare$birth==9999, NA, welfare$birth)
table( !is.na(welfare$age) )

## -------------------------------------------------------------------- ##

welfare$age <- 2015-welfare$birth+1
summary(welfare$age)
qplot(welfare$age)

## -------------------------------------------------------------------- ##

# 나이와 월급의 관계 분석하기
age_income <- welfare %>%
  filter( !is.na(income) ) %>%
  group_by(age) %>%
  summarise( mean_income=mean(income) )

head(age_income)

ggplot(data = age_income, aes(x = age, y = mean_income)) + geom_line()

## -------------------------------------------------------------------- ##

welfare <- welfare %>%
  mutate(ageg=ifelse(age<30, "young",
                     ifelse(age<=59, "middle", "old")) )
table(welfare$ageg)
qplot(welfare$ageg)

## -------------------------------------------------------------------- ##

ageg_income <- welfare %>%
  filter( !is.na(income) ) %>%
  group_by(ageg) %>%
  summarise( mean_income = mean(income) )

ageg_income

ggplot(data = ageg_income, aes(x = ageg, y = mean_income)) + geom_col()
# 그래프 x축 컬럼 순서 조정
ggplot(data = ageg_income, aes(x = ageg, y = mean_income)) + 
  geom_col() +
  scale_x_discrete( limits = c("young", "middle", "old") )


## -------------------------------------------------------------------- ##

# 성별 연령대별 월급 평균표 만들기
sex_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(ageg, sex) %>%
  summarise(mean_income = mean(income))

sex_income

# legend를 하나의 그래프에 표시 fill
ggplot(data = sex_income, aes(x = ageg, y = mean_income, fill = sex)) +
  geom_col() +
  scale_x_discrete(limits = c("young", "middle", "old"))
# legend별 각각의  그래프 그리기
ggplot( data=sex_income, aes(x=ageg, y=mean_income, fill=sex) )+
  geom_col(position="dodge")+
  scale_x_discrete( limits=c("young","middle","old") )

## -------------------------------------------------------------------- ##

# 성별 연령별 월급 평균표 만들기
sex_age <- welfare %>%
  filter( !is.na(income) ) %>%
  group_by(age, sex) %>%
  summarise( mean_income=mean(income) )
head(sex_age)

# 그래프 만들기
ggplot(data = sex_age, aes(x = age, y = mean_income, col = sex)) + geom_line()
