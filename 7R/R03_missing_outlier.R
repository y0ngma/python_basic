## -------------------------------------------------------------------- ##

# MissingValue결측치 정제 하기
df <- data.frame( sex=c("M","F",NA,"M","F"),
                  score=c(5,4,3,4, NA) )
df
is.na(df) # 결측치 확인
table( is.na(df) )
# 결측치 제거하기
warning( library(dplyr) )
df_nomiss <- df %>% filter( !is.na(score) )
mean(df_nomiss$score)
df_nomiss2 <- df %>% filter( !is.na(score)&is.na(sex) )

# 결측치가 하나라도 있으면 제거하기
df_nomiss2 <- na.omit(df)
df_nomiss2

# 함수의 결측치 제외 기능 이용하기
mean( df$scor, na.rm=T ) # 결측치제외하고 평균산출
sum( df$scor, na.rm=T )
# 결측치 생성
exam <- read.csv("./Data/csv_exam.csv")
exam[c(3,8,15), "math"] <- NA
exam
# summarise 활용
exam %>% summarise( mean_math = mean(math) )
exam %>% summarise( mean_math = mean(math, na.rm=T) )
exam %>% summarise( mean_math = mean(math, na.rm=T),
                    sum_math = sum(math, na.rm=T),
                    median_math = median(math, na.rm=T) )

## -------------------------------------------------------------------- ##

# 결측치 대체법(imputation)
## 평균으로 결측치 대체하기
mean( exam$math, na.rm=T )
exam$math <- ifelse( is.na(exam$math), 55, exam$math )
table( is.na(exam$math) )
mean( exam$math ) #대체된 값이랑 결측치제외 평균산출값이랑 비슷한것 확인

## -------------------------------------------------------------------- ##

# Q1. drv구동방식별로 고속도로연비 평균이 다른지 확인
mpg <- as.data.frame(ggplot2::mpg)
#mpg[c(1,2,5), "hwy"] <- NA
head(mpg)
mean( mpg$hwy, na.rm=T )
mpg$hwy <- ifelse( is.na(mpg$hwy), 23, mpg$hwy )
table( is.na(mpg$hwy) )
mean( mpg$hwy )
# Q2. filter()이용 hwy변수 결측치 제외하고 어떤 구동방식이 고속연비좋은가?
mpg %>%
  filter( !is.na(hwy) ) %>%
  group_by(drv) %>%
  summarise( mean_hwy=mean(hwy) )

## -------------------------------------------------------------------- ##

# 이상치 정제 Outlier
# sex 3 이면 NA할당
outlier <- data.frame( sex=c(1,2,1,3,2,1),
                       score=c(5,4,3,1,2,6) )
table(outlier$sex)
table(outlier$score)
outlier$sex <- ifelse(outlier$sex ==3, NA, outlier$sex )
outlier

# score가 1~5아니면 NA 할당
outlier$score <- ifelse(outlier$score >5, NA, outlier$score )
outlier

# 결측치 제외하고 분석
outlier %>%
  filter( !is.na(sex) & !is.na(score) )

outlier %>%
  filter( !is.na(sex) & !is.na(score) ) %>%
#  filter( !is.na(sex) | !is.na(score) ) %>%
  group_by(sex) %>%
  summarise(mean_score = mean(score) )

# 이상치 제거하기 - 극단적인값
# 40~150키로 성인몸무게 벗어나면 극단치
# 통계적 판단 상하위 0.3% 극단치 또는 상자그림 1.5IQR 벗어나면 극단치
## 상자그림으로 극단치 기준 정해서 제거하기
mpg <- as.data.frame(ggplot2::mpg)
boxplot(mpg$hwy)
boxplot(mpg$hwy)$stats

# 12~37(1~5분면 벗아나면 NA할당
mpg$hwy <- ifelse( mpg$hwy<12|mpg$hwy>37, NA, mpg$hwy )
table( is.na(mpg$hwy) )

# 결측치 제외하고 분석
mpg %>%
  group_by(drv) %>%
  summarise( mean_hwy=mean(hwy, na.rm=T) )

## -------------------------------------------------------------------- ##

# mpg데이터에서 구동방식 변수의 값은 4륜, 전륜, 후륜 세종류.
# 몇개의 행에 존재할 수 없는값 k할당
# 도시연비cty에도 극단적 값 할당
mpg <- as.data.frame(ggplot2::mpg)
mpg[c(10,15,58,93), "drv"] <- "k"
mpg[c(29,43,129,203),"cty"] <- c(3,4,39,42)
## Q1. %in%기호 활용, drv의 이상치 결측처리 여부 확인
table(mpg$drv)
mpg$drv <- ifelse( mpg$drv %in% c("4","f","r") ,mpg$drv, NA )
# mpg$drv <- ifelse( mpg$drv!=4|mpg$drv!=f|mpg$drv!=r, NA, mpg$drv )
table(mpg$drv)
table( is.na(mpg$drv) )
## Q2. 상자그림 cty이상치 확인. 결측처리후 다시 상자그림으로 확인
table( is.na(mpg$cty) )
boxplot(mpg$cty)
boxplot(mpg$cty)$stats
mpg$cty <- ifelse( mpg$cty<9|mpg$cty>26, NA, mpg$cty )
table( is.na(mpg$cty) )
boxplot(mpg$cty)
## Q3. 이상치를 제거했으므로 분석할 단계
## drv별 cty평균을 하나의 dplyr문으로 
# df_nomiss2 <- df %>% filter( !is.na(score)&is.na(sex) )
mpg %>% 
  filter( !is.na(drv) & !is.na(cty) ) %>%
  group_by(drv) %>%
  summarise( mean_hwy=mean(cty))
