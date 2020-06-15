##for ~ in ... 문에는 내용을 반복하려는 변수이름과 반복하려는 내용이 담긴다.
''' 정리
#1. 순회할 리스트가 정해져 있을때
for i in listname:
    print(i)

#2. 순회할 횟수가 정해져 있을때
for i in range(len(listname)):
    name = listname[i]
    print(i + 1, name)
    
#3.
for a, b in enumerate(listname):
    print('이름은 {}이고, 번호는 {}이다.'.format(b, a + 1))
'''


patterns = ['가위', '바위', '보','가위', '바위', '보','가위', '바위', '보']
for pattern in patterns: #대입하지 않은 변수 pattern은 for가 만들었다.
    #한줄씩 리스트의 항목을 프린트 하는것이다.
    ''' 이렇게 반복작업의 수고를 덜게 해준다.
    pattern = patterns[0]
    print(pattern)
    pattern = patterns[1]
    print(pattern)
    pattern = patterns[2]
    print(pattern)
    pattern = patterns[3]
    print(pattern)
    pattern = patterns[4]
    print(pattern)
    pattern = patterns[5]
    print(pattern)
    pattern = patterns[6]
    print(pattern)
    pattern = patterns[7]
    print(pattern)
    pattern = patterns[8]
    print(pattern)
    ''' 
    print(pattern) #for ~ in ~ 끝에 : 과 들여쓰기 빼먹지 말자
    
    
    
## 1씩 증가하는 큰수의 그룹만들때 range (큰수)
for i in range(5):
    print(i)

##이름에 번호 붙이기
names   =   ['철수', '영희', '바둑이', '귀두']

for i in range(4): #i는 변수설정 하지 않아도 됨.
    name = names[i] #name 이라는 새변수를 설정할때 리스트 안의 항목으로 하겠다.
    print('{}번 학생: {}'.format(i + 1, name)) #i가 있는 길이4의 항목을 줄마다 출력하되 첫째란에는 1을더한값, 둘째란에는 앞서 설정한 name을.
print()
    
names   =   ['철수', '영희', '바둑이', '귀두', '현희']
for i in range(len(names)): #학생을 추가하였을때 5로 고치기 보다 좋은 방법.
    name = names[i] 
    print('{}번 학생: {}'.format(i + 1, name))
print()

for a, b in enumerate(names): #리스트에 있는 항목에 번호붙이기.
    #print('{}번: {}'. format(a + 1, b))
    print(a + 1)
    print(b)
    
for i in range(300):
    print(chr(44032 + i), end='') #가 라는 글자 번호 #end는 줄바꾸기 + ''안의 값(빈칸) 넣기 인듯
    