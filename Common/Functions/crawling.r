## -------------------------------------------------------------------- ##
# 키워드로 네이버모바일페이지에서 주소, 좌표 가져오기

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