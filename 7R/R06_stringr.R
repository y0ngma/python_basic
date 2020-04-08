## -------------------------------------------------------------------- ##
#stringr은tidyverse 패키지에 포함된 글자조작용 패키지로 ICU라고 불리는
#C library의 wrapper인 stringi패키지 기반

# install.packages("Rcpp")
# install.packages("usethis")
# install.packages("glue")
# install.packages("devtolls")
# library(devtools)
# install.packages("remotes")
# library(remotes)

# install_github("mrchypark/tqk")
# library(tqk)

# if ( !require(tidyverse) ) install.packages("tidyverse")
# install.packages('stringr')

# install_github("mrchypark/krwifi")
# library(krwifi)

library(stringr)
library(dplyr)

load("./Data/wifi.rda")
ls()
head(wifi,5)

krwifi <- wifi

# sapply는 list대신 행렬 또는 벡터로 반환한다
# lapply는 list 반환
wifi %>%
  distinct(소재지도로명주소) %>%
  slice(1:10) %>%
  mutate( len=str_length(소재지도로명주소), # str길이 세기
          gun_count=str_count(소재지도로명주소, "군"),
          addr1=str_split(소재지도로명주소, " ") %>% sapply(function(x) x[1]),
          addr2=str_split(소재지도로명주소, " ") %>% sapply(function(x) x[2]),
          addr3=str_split(소재지도로명주소, " ") %>% sapply(function(x) x[3]),
          # 자른것을 x로 받아서 그것의 3번째 것에 접근
          trunc=str_trunc(소재지도로명주소, width=14) )#14자 이상길이는 "..."처리

wifi %>%
  distinct(설치시군구명) %>%
  slice(1:10) %>%
  mutate( repla=str_replace(설치시군구명, "군", "도로시"),
          extra=str_extract(설치시군구명, "주시"),
          start=str_locate(설치시군구명, "구|군") %>% .[,1],
          end=str_locate(설치시군구명, "구|군") %>% .[,2],#xx구군일때 start=3,end=4
          remove=str_remove(설치시군구명, "구|군|시"),
          if_remove=if_else( str_length(설치시군구명)==2,
                             설치시군구명,
                             str_remove(설치시군구명, "구|군|시") )
          )

# filter()와 함께사용하는 함수
wifi %>%
  filter( str_detect(소재지도로명주소, "군") ) %>%
  slice(1:1)

wifi %>%
  filter( str_starts(설치장소상세, "민원") ) %>%
  distinct(설치장소상세)

wifi %>%
  filter( str_starts(설치장소상세, "민원") ) %>%
  group_by(설치장소상세) %>%
  summarise(n=n())%>%
  arrange(desc(n))

## -------------------------------------------------------------------- ##

# 공백제거
str_trim("           hello    world!           ")
str_trim("           hello    world!           ", side="left")
str_trim("           hello    world!           ", side="right")
str_squish("         hello    world!           ")

str_trim(" String with trailing and leading white space\t")
str_trim("\n\nString with trailing and leading white space\n\n")
str_squish("  String with trailing and leading white space")

## -------------------------------------------------------------------- ##

# 한글인코딩 (윈도우용) 
# cp949(ms949라고도 불림. 웹에서 euc-kr도 있음)와 utf-8(UTF-8)
# 인코딩은 데이터자체인 바이트단위기록 그자체와 해석법이라는 메타데이터로 이루어짐

## 변수/ 값 삭제 
rm(list=c('tem', 'tem_uft')) # varA, varB 변수 삭제 
rm(list=ls(all=TRUE)) # 메모리에 로딩되어있는 모든 변수 삭제 

tem <- "안녕 하세요"
tem
Encoding(tem)
Encoding(tem) <- "UTF-8"
Encoding(tem)
tem

tem_utf <- iconv(tem, to="UTF-8")
tem_utf
Encoding(tem_utf)
tem_utf

## -------------------------------------------------------------------- ##

wifi %>%
  distinct(설치시군구명) %>%
  slice(1:10) %>%
  transmute( iconv_utf8=str_conv(설치시군구명, "utf8"),
             iconv_cp949=str_conv(설치시군구명, "cp949") )

wifi %>%
  with( Encoding(설치시군구명) %>%
         table() %>%
         as_tibble() )

wifi %>%
  distinct(설치시군구명) %>%
  filter( Encoding(설치시군구명)=="unknown" )

## -------------------------------------------------------------------- ##



