## -------------------------------------------------------------------- ##
library(ggplot2)
library(dplyr)

## geom_point() 점그래프.
ggplot(data = mpg, aes(x = displ, y = hwy))# 지정해 배경 생성
ggplot(data = mpg, aes(x = displ, y = hwy)) + geom_point()# 배경에 산점도 추가
ggplot(data = mpg, aes(x = displ, y = hwy)) + geom_point() + xlim(3, 6)
# x축 범위 3~6, y축 범위 10~30으로 지정
ggplot(data = mpg, aes(x = displ, y = hwy)) + 
  geom_point() + 
  xlim(3, 6) + 
  ylim(10, 30)

# x축 범위 y축 범위 넓히기. 
ggplot( data=midwest, aes(x=poptotal, y=popasian) ) +
  geom_point() +
  xlim(0, 500000) +
  ylim(0, 2000)

## -------------------------------------------------------------------- ##

## geom_bar()빈도 막대그래프 
ggplot( data = mpg, aes(x = drv)) + geom_bar()
ggplot( data = mpg, aes(x = hwy) ) + geom_bar()

# geom_col()막대그래프 - 집단간 차이
## 평균막대그래프 그리기
## 1. 집단의 평균표 만들기
df_mpg <- mpg %>%
  group_by(drv) %>%
  summarise(mean_hwy=mean(hwy))

df_mpg
## 2. 그래프생성
ggplot( data=df_mpg, aes(x=drv, y=mean_hwy) ) + geom_col()
## 3. 크기순으로 정렬('-'있고없고 차이 비교)
#ggplot( data=df_mpg, aes(x=reorder(drv,mean_hwy), y=mean_hwy) ) +geom_col()
ggplot( data=df_mpg, aes(x=reorder(drv,-mean_hwy), y=mean_hwy) ) +geom_col()

## -------------------------------------------------------------------- ##

## 선그래프 
ggplot(data = economics, aes(x = date, y = unemploy)) + geom_line()

## 5.상자 그림
ggplot(data = mpg, aes(x = drv, y = hwy)) + geom_boxplot()

## -------------------------------------------------------------------- ##

## Q1. 어떤회사suv차종의 도시연비가 높나? 다섯곳막대 연비순정렬
df<- mpg %>%
  filter( class == 'suv' ) %>%
  group_by(manufacturer) %>%
  summarise( mean_cty=mean(cty) ) %>%
  arrange( desc(mean_cty) ) %>%
  head(5)
ggplot( data=df, aes(x=manufacturer, y=mean_cty) ) + geom_col()
#ggplot( data=df, aes(x=reorder(manufacturer, -mean_cty), y=mean_cty) ) + geom_col()

## -------------------------------------------------------------------- ##

