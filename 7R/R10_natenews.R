## -------------------------------------------------------------------- ##
rm(list=ls(all=TRUE))

# 네이트뉴스 가져오기
# 인코딩 안될때 b3<-repair_encoding(b2)
install.packages('stringr')
install.packages('rvest')

library(stringr)
library(dplyr)
library(rvest)

## -------------------------------------------------------------------- ##

x <- 0
dadate <- as.Date(Sys.time() )-x # 현재날짜
dadate <- gsub("0", "",dadate)

day_url <- NULL
day_title <- NULL
i <- NULL
final_data <- NULL # 초기화

for(i in 1:10) {
  path  <- "https://news.nate.com/recent?mid=n0100&type=c&"
  url   <- paste0(path, date, "&page=", i)
  # date=20200409
  
} 
  b     <- readLines(url, encoding="EUC-KR")
  bb <- repair_encoding(b)
  head(bb, 10)

  # 제목가져오기
  # <strong class="tit">'막말 제명'</strong>  
  b2    <- b[str_detect(b, "strong class=\"tit\"")]
  # str(b2)
  # b3<-repair_encoding(b2)
  head(b2, 10)
  # (?<=시작) ... (?=<끝)
  #  \" 는 을 문자열로 인식하게 함
  title <- str_extract(b2, ("(?<=<strong class=\"tit\">).*(?=</strong>)") )
  str(title)
  b3    <- b[str_detect(b, '<strong class="hit">') ]
  b3    <- b[str_detect(b, "<strong class=\"hit\">")] # 동일결과
  # str(b3)
  
  # 공지글의 조회수가 포함되어 1,2 번쨰 데이터는 빼고 읽어옴
  hit   <- str_extract(b3, ("(?<=\">).*(?=</strong>)"))[-1:-2]
  # hit
  
  b4    <- str_split(b3, "hit\">")
  hit   <- str_sub(sapply(b4, function(x){x[2]}), end=-8)
  # <a class> 추출 확인
  b5    <- b[which(str_detect(b, "subject_fixed"))-2]
  # str(b5)
  
  # href 가져오기
  b6    <- str_sub(str_extract(b5, ("(?<=href=\").*(?=data-role)")), end=-4)
  # str(b6)
  
  # 글내용 접속 URL
  url   <- paste0("https://www.clien.net", b6)
  data  <- cbind(title, hit, url)
  # data
  
  final_data <- rbind(final_data, data)
  # length(title)
  # length(hit)
  # length(url)
  
  cat("\n", i)

dim(final_data)
head(final_data)
tail(final_data)

# 글목록 데이터 저장
setwd("./")
write.csv( final_data, "./Data/base_data1.csv", row.names=F )

## -------------------------------------------------------------------- ##

# 글목록수집데이터에서 글본문 링크로 글 본문 수집
setwd("./")
data <- read.csv("./Data/base_data1.csv")
head(data)
# save(data, file="base_data.RData")
# load("base_data.RData")

library(stringr)
url_list <- data[,3]

length(url_list)
content <- c()
for(i in 1:length(url_list)) {
  b <- readLines(as.character(url_list[1]), encoding="UTF-8")
  if(class(try(b <- readLines(as.character(url_list[i]), encoding="UTF-8"))) == "try-error")  {
    b6 <- ""
    content <- c(content, b6)
  }else{
    b2 <- b[which(str_detect(b, "post_content")):which(str_detect(b, "post_ccls"))]
    b3 <- paste(b2, collapse="")
    # str(b3)
    b4 <- gsub("<.*?>", "", b3)
    # str(b4)
    b5 <- gsub("\t|&nbsp;", "", b4)
    # str(b5)
    b6 <- str_trim(b5)
    content <- c(content, b6)
    cat("\n", i)
  }
}
head(content)

final_data <- cbind(data, content)

setwd("./")
write.csv(final_data, "final_data.csv", row.names=F)

