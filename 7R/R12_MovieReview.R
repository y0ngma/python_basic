## -------------------------------------------------------------------- ##

library(stringr)
score_list <-list()
text_list <- list()

for(i in 1:2500){
  i<-1
  path<-"https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=190568&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="
  url<-paste0(path, i)
  url
  
  b<-readLines(url,encoding="UTF-8")
  head(b, 12)
  
  b2<-b[which(str_detect(b,"star_score"))+2]#평점찾기
  b2
  
  str_extract(b2,("(?<=<em>).*(</em>)"))
  str_sub(str_extract(b2,("(?<=<em>).*(</em>)")),end=-6)
  score<-as.numeric(str_sub(str_extract(b2,("(?<=<em>).*(</em>)")),end=-6))
  score
  
  #<span id="_filtered_ment_8"> ... </span>
  score_list[[i]] <-score
  
  which(str_detect(b,"<span id=\"_filtered_ment_"))+4
  text<-b[which(str_detect(b,"<span id=\"_filtered_ment_"))+4]
  head(text)
  
  text2<-gsub("\t", "", text)
  head(text2)
  
  #자바스크립트 없애기
  str_sub(text2[str_detect(text2, "javascript")], 42, end=-36)
  text2[str_detect(text2, "javascript")]<-str_sub(text2[str_detect(text2, "javascript")], 42, end=-36)
  head(text2)
  text_list[[i]] <-text2
  cat("\n", i)
  
  if(i %% 500==0){
    cat("\n save ",i)
    final_score<-unlist(score_list)
    head(final_score)
    final_text<-unlist(text_list)
    
    # 현경로에 500개씩 저장
    setwd("./")
    save(final_score, file="final_score.RData")
    save(final_text, file="final_text.RData")
  }
}
# 해당경로에 한번에 모두 저장
setwd("./")
save(final_score, file="./Data/movie/final_score.RData")
save(final_text, file="./Data/movie/final_text.RData")


