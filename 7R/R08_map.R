## -------------------------------------------------------------------- ##
rm(list=ls(all=TRUE))
install.packages("RJSONIO")
library(RJSONIO)

keyword = '부산 대학교 캠퍼스'

loc <- iconv( keyword, from="cp949", to="UTF-8" ) # 윈도 키워드인코딩 변화
juso <- URLencode(loc)

# 모바일 네이버 지도 활용(네이버지도는 막혀있음)
url<-paste0("https://m.map.naver.com/search2/searchMore.nhn?query=",
            juso,"&sm=clk&page=1&displayCount=75&type=SITE_1")

url

# ctrl shift 로 경로를 찾을 수 있다
b <- readLines( url, encoding="UTF-8" )

b2 <- paste( b, collapse=" " ) #JSON형태라서 R에서 list로 변환
head(b2[1])

b3 <- fromJSON(b2) # list로 변환
head(b3)[1]

# x, y 좌표 찾기
wg <- c( b3$result$site$list[[1]]$x,b3$result$site$list[[1]]$y )

## -------------------------------------------------------------------- ##

search_loc <- function(keyword){
  loc  <- iconv( keyword, from="cp949", to="UTF-8" ) # 윈도 키워드인코딩 변화
  juso <- URLencode(loc)
  url  <-paste0("https://m.map.naver.com/search2/searchMore.nhn?query=",
              juso,"&sm=clk&page=1&displayCount=75&type=SITE_1")
  b    <- readLines( url, encoding="UTF-8" )
  b2   <- paste( b, collapse=" " ) #JSON형태라서 R에서 list로 변환
  b3   <- fromJSON(b2) # list로 변환
  # x, y 좌표 찾기
  # JSON 요소는 $으로 접근가능
  wg   <- c( b3$result$site$list[[1]]$x, b3$result$site$list[[1]]$y )
  return(wg)
}

search_address <- function(keyword){
  loc  <- iconv( keyword, from="cp949", to="UTF-8" ) # 윈도 키워드인코딩 변화
  juso <- URLencode(loc)
  url  <-paste0("https://m.map.naver.com/search2/searchMore.nhn?query=",
              juso,"&sm=clk&page=1&displayCount=75&type=SITE_1")
  b    <- readLines( url, encoding="UTF-8" )
  b2   <- paste( b, collapse=" " )
  b3   <- fromJSON(b2)
  wg   <- c( b3$result$site$list[[1]]$address ) # 주소 찾기
  return(wg)
}

search_loc('부산대')
search_address('부산대')

