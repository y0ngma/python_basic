
list1 = ['가위', '바위', '보']
list2 = [0, 1, 2, 3, 4, 5]

print(list1[0]) #건물이 0층부터 시작하면 10층 갈때 10층계 올라가면 된다. 0부터 시작이 편리한 이유!!
print(list2[-1]) #뒤에서 1번째
print(list1[-3]) 
#print(list1[-4])#뒤에서 4번쨰는 없으므로 에러



'''
list2.append(6) #마지막에 추가하는법
print(list2)

'''


#새로운 리스트를 만드는 방법
list3 = list2 + [6]
print(list3)

list4 = list2 + list3
list5 = list3 + list2
print(list4)
print(list5)


##있나 없나 확인법
n = 12
ownership = n in list2
print(ownership)

n = 10
if n in list2:
    print('{}은 있어!'.format(n))
else:
    print('{}은 없어!'.format(n))

##리스트 안의 값 제거방법 2가지    
print('처음 list4는    :', list4)
del (list4[0])
print('[0]을 뺀 list4는:', list4)

list4.remove(3)
print('항목3을 뺀 list4:', list4)#처음 나오는 3만 제거된다.


