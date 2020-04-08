
# 글 본문 데이터를 이용하여 형태소 분석 및 워드 클라우드
setwd("./")
final_data <- read.csv("./Data/final_data.csv", encoding="EUC-KR", fileEncoding="EUC-KR")
#final_data <- read.csv("./Data/final_data.csv", encoding="cp949", fileEncoding="UTF-8")
#final_data <- read.csv("./final_data.csv")
head(data)
install.packages("KoNLP")
install.packages("wordcloud")

library(KoNLP) # 한글 형태소 분석기
library(dplyr) # 데이터프레임 다루는 라이브러리
# useNIADic()  # 사전 데이터
library(stringr) # 텍스 처리 라이브러리
library(RColorBrewer) # 칼라 팔레트
library(wordcloud) # 워드클라우드 라이브러리
txt <- str_replace_all(final_data[,4], "\\W", " ")
str(txt)
nouns <- extractNoun(txt)
head(nouns)
wordcount <- table(unlist(nouns))
wordcount
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
str(df_word)
df_word <- rename(df_word, word = Var1, freq = Freq)
str(df_word)
df_word <- filter(df_word, nchar(word) >= 2)
top_20 <- df_word %>% arrange(desc(freq)) %>% head(20)
top_20

?brewer.pal
pal <- brewer.pal(8,"Dark2")
set.seed(1234)

wordcloud(words = df_word$word, # 단어 
          freq = df_word$freq, # 빈도 
          min.freq = 2, # 최소 단어 빈도 
          max.words = 200, # 표현 단어 수 
          random.order = F, # 고빈도 단어 중앙 배치 
          rot.per = .1, # 회전 단어 비율 
          scale = c(4, 0.3), # 단어 크기 범위 
          colors = pal) # 색깔 목록