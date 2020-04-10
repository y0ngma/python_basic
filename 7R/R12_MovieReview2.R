## -------------------------------------------------------------------- ##

library(stringr)
library(dplyr)

setwd("./")
load("./Data/movie/final_score.RData")
load("./Data/movie/final_text.RData")

head(final_score)
head(final_text)

# 불용어 제거
comments<-gsub("<.*?>","", final_text) # 원하는텍스파일명
comments<-gsub("\t","",comments)
comments<-gsub("[][!#$%*,:;<=>@_`|‘~{}&★☆ㅋㅎ《》◈△▲▽▼○●◎◇◆□◁◀▷▶♤♠♡♥♧♣◉◈▣◐◑♨☏☎☜☞↖↘♭♩♪♬㈜]", " ",comments)
comments<-gsub("rdquo|gt|lt|nbsp|amp|quot|apos","",comments)
comments<-gsub("  "," ",comments)
comments<-gsub("\\^"," ",comments)
comments<-gsub("ㅠ|ㅜ|ㅡ"," ",comments)
comments<-gsub("\"|\n|+","",comments)
comments<-gsub("\\+","",comments)
comments<-gsub("/|!|\\*|\\+|\\@"," ",comments)
comments<-gsub("'","",comments)
comments<-gsub("\"","",comments)
comments<-gsub("\"","",comments)
comments<-gsub("=","",comments)
comments<-gsub("~|;|<|>","",comments)
comments<-gsub("\\?","",comments)
comments<-gsub("\\[.*?\\]","",comments)
comments<-gsub("\\(.*?\\)","",comments)
comments<-gsub("\\(|\\)"," ",comments)
comments<-gsub("\\]|\\[|\\(|\\)|:|-|\\,|\\."," ",comments)
comments<-gsub("\\!","",comments)
comments<-gsub("\"\"","",comments)
er<-c("","것","원","저","년","역","나","이","수","월","한","동","대","전","층","들","때",
      "개","분","적","후","점","시","별","보건증","곳","번","해서","쪽","데","말","시작","우리",
      "이번","중","지원","사러가기","명","주","기","소","률","판","판매목표","구","지금샵","co","kr","com","무단전재","저작권자",
      "일","or","드","뭐","백","천","듯","만","우","잭","거","애","등","두","타","to","the","copyrights","properties","var",
      "내","제","함","지","라","안","혜")
head(comments)

## -------------------------------------------------------------------- ##

#dtm(Document-term Matrix)
# 해당문서의 해당용어의 출현빈도를 카운팅해서 행렬화

co<-str_split(comments, " ")
head(co)
co2<-table(unlist(co))
length(co2)
wo<-names(sort(co2, decreasing=T)[2:301])
head(wo)
wo<-wo[ !str_detect(wo, "\\d")]
head(wo)

## -------------------------------------------------------------------- ##

i<-1
mat<-matrix( 0, ncol=length(wo), nrow=length(co) )
head(mat)

# 원핫인코딩으로 문자를 벡터화
for( i in 1:length(co) ){
  mat[ i, wo %in% co[[i]] ]<-1
  cat( "\n", i )
}
colnames(mat)<-wo

mat<-data.frame(mat)
head(mat)

mat2<-mat[ apply(mat, 1, sum)>0, ]
head(mat2)

score2<-final_score[ apply(mat, 1, sum)>0 ]

table(score2)
hist(score2)

score3<-ifelse( score2>5,1,0 )

dim(mat2)
length(mat2)

## -------------------------------------------------------------------- ##

sam<-sample( 1:nrow(mat2), nrow(mat2)*0.7 )
train<-mat2[sam,]
valid<-mat2[-sam,]
tr_y<-score3[sam]
valid_y<-score3[-sam]

# lasso(numeric method) -> 회귀계수0
# ridge(analyric)->회귀계수에 가깝게만
# shriankage regression 회귀계수 축소법
# lambda의 크기에 따라 회귀계수가 0으로 가는 비율이 결정됨
# glmnet
# alpha=0 lasso / alpha=1ridge / 0 < alpha< 1 elastic net
install.packages("glmnet")
library(glmnet)

pr1<-0
pr2<-0
acc_list<-NULL
# for(i in 1:10){}
# 훈련데이터 로우수 가져오기
ss <-sample(1:nrow(train), nrow(train), replace=F)
head(ss)
# 훈련데이터 컬럼수 가져오기
vv<-sample( 1:ncol(train), ncol(train)*1 )
head(vv)

# 리지 
fit1=glmnet( as.matrix(train[ss,vv]),
             tr_y[ss], family="binomial",
             alpha=1,
             nlambda=50 )

s1<-fit1$lambda[ length(fit1$lambda) ]
cos<-coef(fit1, s=s1) # extract coefficients at a single value
sort( cos[,1], decreasing=T )[1:30] # 긍정
sort( cos[,1], decreasing=F )[1:30] # 부정

pr<-predict( fit1, as.matrix(valid[,vv]), s=s1 )
head(pr)

# 오차
pr1<-pr1+pr # 누적
pred<-ifelse(pr1/i>0, 1, 0)

# 정확도
acc1<-sum(pred==valid_y)/length(valid_y) 
acc1

## -------------------------------------------------------------------- ##

# 라쏘 
fit2=glmnet( as.matrix(train[ss,vv]),
             tr_y[ss], family="binomial",
             alpha=1,
             nlambda=50 )

s1<-fit2$lambda[ length(fit2$lambda) ]
cos<-coef(fit2, s=s1) # extract coefficients at a single value
sort( cos[,1], decreasing=T )[1:30] # 긍정
sort( cos[,1], decreasing=F )[1:30] # 부정
pr<-predict( fit2, as.matrix(valid[,vv]), s=s1 )
head(pr)

# 오차
pr2<-pr2+pr # 누적
pred<-ifelse(pr2/i>0, 1, 0)

# 정확도
acc2<-sum(pred==valid_y)/length(valid_y) 
acc2

## -------------------------------------------------------------------- ##

acc_list<-rbind( acc_list,c(acc1,acc2) )
ts.plot( acc_list, col=c("red", "blue") )
cat("\n", i)


# 랜덤포레스트
install.packages("randomForest")
library(randomForest)

# classification
# data(iris)
train<-mat2[sam,]
valid<-mat2[-sam,]
tr_y<-score3[sam]
valid_y<-score3[-sam]

data1<-cbind(train,tr_y)
head(data1)

fit_rf <- randomForest(tr_y~., data=data1,
                       importance=TRUE,
                       do.trace=T,
                       ntree=300, #의사결정트리
                       proximity=TRUE)
print(fit_rf)

# Look at variable importance:
round(importance(fit_rf), 2) # 반올림

pr<-predict(fit_rf, valid)
head(pr)
hist(pr)
pred<-ifelse(pr>0.5, 1, 0)
sum(pred==valid_y)/length(valid_y) # 0.7595916

