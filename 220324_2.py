# while, for문을 이용해 list이용하기
from re import S


list1 = [10,22,33,44,55,66,77,88,99,100]
list2 = [11,22,33,4499,54,56,88,10]
# 1. while문으로 모든 값을 출력해주세요.
n = 0
while n < len(list1) :
    print(list1[n])
    n+=1

# 2. 위 리스트를 for문을 이용해 출력해주세요.
for n in list1 :
    print(n)
# 3. 위 리스트를 for문을 이용해 3의 배수만 출력해주세요.
for n in list1 :
    if n %3 == 0:
        print(n)
# 4. 위 리스트를 for문을 이용해 리스트의 모든 값들을 더한 값을 출력해주세요.
# while 버전, for .. in 버전
m = 0
s = 0
while m < len(list1):
    
    s += list1[m]
    m +=1 
print(s)    

tatal = 0
for n in list1 :
    tatal += n
    

print(tatal)


# 문제 - 999단을 출력해주세요.
"""
1 * 1 * 1 = 1
1 * 1 * 2 = 2
1 * 1 * 9 = 9
1 * 2 * 1 = 2
1 * 2 * 2 = 4
....
2 * 1 *  1 = 2
....
....
....
9 * 9 * 8 = 648
9 * 9 * 9 = 729
"""
# for a in range(1,10,1) :
#     for b in range(1,10,1) :
#         for c in range(1,10,1) :
#             print("{} * {} * {} = {}".format(a,b,c,a*b*c))


# 파이썬 내장함수
print(sum(list1))





# 사용자 정의함수
def my_sum() :
    total = 0
    for num in list1 :
        total += num
    print(total)


# 사용자 함수의 좋은점 
# 코드가 보기 편해진다.
# 코드가 단단해짐 ==> 코드 구조화
# 코드를 여러번 바꾸지 않아도 된다. ==> 코드의 재사용
my_sum()

print("\n")

def add1(x) :
    total = 0
    for num in x :
        total += num
    print(total)

add1(list2)
add1(list1)


def add2(a,b,c):
    k = 0
    k = a + b + c
    print(k)
add2(5,6,11)