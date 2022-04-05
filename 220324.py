# list_ 관련 함수

# 1. insert 함수 --> 어디든 추가 가능
from msvcrt import kbhit


a = [1,2,3,4,5,6,8,9,10]

a.insert(6,7)
print(a)

# 2. append --> 리스트의 가장 뒤에 추가됨, 주의! 한번에 한개만 입력 가능, 이중리스트 구현은 가능
a.append("오백")
a.append([55,66,99,44,212])

print(a)

# 3. pop --> 리스트 가장 끝에 있는 원소 꺼내기

a.pop()

print(a)

print(a.pop())


# 문제

list1 = [2,5,9,11,23,51,26,38,41,93,101]

# 위 리스트의 모든 값을 출력해주세요.
# 출력 : 2, 5, 9, 11, 23, 51, 26, 38, 41, 93, 101
print(list1)

# 위 리스트의 '홀수번째 인덱스' 값만 출력해주세요.
# 출력 : 5, 11, 51, 38, 93

n = 1
while n < len(list1) :
    print(list1[n])
    n+=2



# 위 리스트의 '짝수값'만 출력해주세요. 
# 출력 : 2, 26, 38
b = 0

while b < len(list1) :
    if list1[b] %2 == 0 :
        
        print(list1[b])
    b+=1

# 위 리스트의 값으로 구구단을 만들어주세요
# 출력 : 2단, 5단, 9단, 11단, 23단, 51단, 26단, 38단, 41단, 93단, 101단


# dan = [2, 5, 9, 11, 23, 51, 26, 38, 41, 93, 101]

# i = 1

# while i < len(dan) :
    
#     d = 1
#     while d <= 9 :
#         print("{} * {} = {}".format(d, dan[i], d*dan[i]))
#         d += 1
    
    
#     i += 1
    




# 위 리스트의 값을 거꾸로 출력해주세요.
# 출력 : 101, 93, 41, 38, 26, 51, 23, 11, 9, 5, 2

i = len(list1)-1

while i >= 0 :
    print(list1[i])
    i -= 1
    




#  1 ~ 10 까지 수 리스트 선언 
l= []
k = 1
while k <= 10 :
    l.append(k)
    k += 1
print(l)


# 리스트 값 짝수만 가져오기
n = 1
while n < len(l) :
    
    
    if l[n] % 2 == 0 :
        print(l[n])
    n += 1

# 리스트에 11, 13, 15 추가하기

l.append(11)
l.append(13)
l.append(15)

# 리스트의 짝수번째 값 1증가시키기
print(l)
n=0
while n < len(l) :
    if n % 2 == 0 :
        l[n] += 1
    n += 1
print(l)
    

# 리스트에서 세번째 값 지우기

del l[2]

print(l)


