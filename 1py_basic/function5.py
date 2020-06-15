#함수내의 return의 사용법
def add(a,b):
    r1 = a + b
    r2 = a - b
    
    return r1, r2 #함수정의 시 2가지 모두 사용하려면,

x = 1
y = 2
z = 3.5
k = 3.4

r1, r2 = add(x, y) #함수호출 시 r1, r2모두 써준다!
print('답은 {} {}'. format(r1, r2))


