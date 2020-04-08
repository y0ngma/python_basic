## -------------------------------------------------------------------- ##
rm(list=ls(all=TRUE))

# 클리앙의 모두의 공원 게시글을 수집하는 코드
# html소스를 보면서 해야 이해가 빠름
# 긁고자 하는 사이트에서 오른쪽마우스클릭 -> 소스보기
# 규칙을 찾아 원하는 정보만 추출
install.packages('stringr')
library(stringr)
library(dplyr)

## -------------------------------------------------------------------- ##

final_data <- NULL # 초기화

for(i in 1:10) {
  path  <- "https://www.clien.net/service/board/park?&od=T31&po="
  url   <- paste0(path, i-1)
  b     <- readLines(url, encoding="UTF-8")
  # str(source)
  # length(source)
  # head(source, 10)
  
  # 게시판의 글 제목 우클릭-검사 하면 
  # <span class="subject_fixed" data-role="list-title-text" title="오늘..
  b2    <- b[str_detect(b, "subject_fixed")]
  # str(b2)
  
  title <- str_extract(b2, ("(?<=\">).*(?=</span>)"))
  # str(title)
  
  #  \" 는 을 문자열로 인식하게 함
  b3    <- b[str_detect(b, '<span class="hit">') ]
  b3    <- b[str_detect(b, "<span class=\"hit\">")] # 동일결과
  # str(b3)
  
  # 공지글의 조회수가 포함되어 1,2 번쨰 데이터는 빼고 읽어옴
  hit   <- str_extract(b3, ("(?<=\">).*(?=</span>)"))[-1:-2]
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
}

dim(final_data)
head(final_data)
tail(final_data)

# 글목록 데이터 저장
setwd("./")
write.csv( final_data, "./Data/base_data.csv", row.names=F )

## -------------------------------------------------------------------- ##

# 글목록수집데이터에서 글본문 링크로 글 본문 수집
setwd("./")
data <- read.csv("./Data/base_data.csv")
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
  
