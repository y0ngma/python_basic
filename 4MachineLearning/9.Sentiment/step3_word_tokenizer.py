from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk

# stopword 단어 사전을 다운
nltk.download('stopwords')
# stopword 데이터 가져오기
stop = stopwords.words('german')
# 단어 줄기를 하기위한 객체
porter = PorterStemmer()

# 공백으로 단어분리
def tokenizer(text):
    return text.split()

# 단어줄기
def tokenizer_porter(text):
    # 띄어쓰기를 기준으로 분리한다
    word_list = text.split()
    # 단어 줄기(어간) 처리
    # he has -> have
    word_list2 = [porter.stem(word) for word in word_list]
    return word_list2

def tokenizer_stopwordsr(text):
    # 띄어쓰기를 기준으로 분리한다.
    word_list = text.split()
    #단어 줄기 처리
    word_list2 = [porter.stem(word) for word in word_list]
    # 불용어 처리
    result =[]
    for w in word_list2:
        if w not in stop:
            result.append(w)

    return result

def step3_word_tokenizer():
    # text = 'runners like running and thus they run'
    text = 'Möchtest du ein Bier trinken?'
    # text = 'Я люблю тебя.'
    # text = 'わたしは、あなたを愛しています'
    # text = '나는 너를 좋아한다.'
    a1 = tokenizer(text)
    a2 = tokenizer_porter(text)
    print('a1 :', a1)
    print('a2 : ', a2)
