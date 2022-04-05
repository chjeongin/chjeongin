# 소스코드 4대 요소 --> 자료, 변수, 조건, 반복
# 반복문

# 반복문 제어 --> 횟수 세기

# a = 5 #반복 횟수 --> while 안에 있으면 다시 초기화되므로 밖에 있어야함.
# while a <= 10 : #조건 입력
#     print(a)
    
#     a += 5
    

# 수열 만들기 (변수 --> 시작값, 조건식 값 --> 마침값)

# 마라탕, 떡볶이, 피자, 배스킨라빈스 아몬드봉봉 


# 문제 : 99단 8단을 출력해주세요.
# 조건 : while문을 사용해주세요.

"""
출력 양식 
== 8단 ==
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
"""



# 수정가능 시작
from re import I


print("== 8단 ==")
c = 1
while c <= 9:
    print("8 * {} = {}".format(c, c*8))
    c += 1

print("\n")

# 1 ~ 100까지 출력
# a = 1
# while a <= 100 :
#     print(a, end =" ")
#     a +=1

# print("\n")

# # 2. -25 ~ 50까지 출력

# b = -25
# while b <= 50:
#     print(b, end =" ")
#     b+=1

# print("\n")

# # 1. 1 ~ 100 까지 짝수만 출력
# for num in range(2, 101, 2) :
#   print(num, end=" ")

# print("\n")

# a=2
# while a <= 100:
#     print(a, end=" ")
#     a+=2
# print("\n")

# num = 1
# while num <= 100:
#     if num %2 ==0:
#         print(num)
# print("\n")

# 2. 100 ~ 200 사이의 홀수만 출력
for a in range(101, 201, 2) :
    print(a, end=" ")

print("\n")

# a = 101
# while a <= 200 :
#     print(a, end=" ")
#     a += 1
print("\n")



# 1 ~ 500 사이의 수 중 4의 배수만 출력
# d = 4
# while d <= 500 :
#     print(d, end=" ")
#     d += 4







'''
축구 경기가 진행중이다. 축구경기 타임은 총 90분이고,

현재 A팀이 0점, B팀이 2점인 상황에서, A팀은 최고의 스트라이커인 손흥민을 투입하기로 결정했다.

손흥민은 투입과 동시에 그리고 5분마다 골을 넣을 수 있는 능력을 가지고 있다.

만약 80분에 투입이 되면 80분에 곧바로 골을 넣게되고 85분에 골을 넣음으로서 동점이 가능하게 된다.

(90분이되면 경기가 바로 종료되므로 골을 넣을 수 없다. 해당 경기의 심판은 추가시간을 주지 않는 것으로 유명하다.)

현재 경기타임 time과 A팀의 득점 score가 주어질 때, 손흥민을 투입하면 A팀의 최종 득점은 몇 점인지 출력하시오.
'''
time = 74
score = 0

# 출력 : 4
end = 90
b = 5
while time < 90 :
    score += 1
    time +=5
print(score)



# 100까지의 합
# k = 0
# while k < 100 :
#     s = s + i
#     i = i + 1
#     k += 1
    

k = 0
i = 0
while i <= 100 :
    k = i + k
    i += 1
    
print(k)

print("\n")

# 구구단 2~9단 출력해주세요.

print("구구단")

num = 2
while num <= 9 :
    dan = num
    i = 1
    while i <= 9 :
       print("{} * {} = {}".format(dan, i, dan*i))
       i += 1
    num += 1 

print("\n")

# n과 m 사이의 수 중 k의 배수 출력
n = 10
m = 30
k = 3

a = n
end = m
while a <= end :
    

    print(a)
    a += k
    
print("\n")

# 반복문 --> 코드를 원하는 만큼 반복, 수열(규칙)을 만들 수 있다.

# 학생들의 성적
# 철수 86점, 영희 90점 선빈 100점, 진희 70점. 길동 50점

# 변수가 많아지면 변수관리가 어려움
# 변수는 규칙적으로 사용이 어려움(일괄처리가 힘들다)
# 학생들에게 번호를 부여

# 여러개의 데이터를 하나의 변수에 순서(index)를 부여해서 저장 --> 리스트
A_class = [86, 90, 100, 70, 50]


# 파이썬은 순서를 0부터 센다.

# 파이썬 리스트의 마지막 번호는 리스트 원소 개수 -1 (규칙)



# 0번부터 4번까지 호출
print(A_class[0])
print(A_class[1])
print(A_class[2])
print(A_class[3])
print(A_class[4])

print("\n")

i = 0
while i <= 4:
    print(A_class[i])
    i += 1


# A반 학생들의 평균 점수

s = 0
i = 0

while i <= 4:
    s += A_class[i]
    i += 1

print(s/5)

print("\n")


# list 선언
list1 = [1,2,3,5,55.1]
list2 = ["마라탕", "치킨", "피자", "오렌지", "파스타"]
list3=[]

print(list1[4])

print(list3)

list1 = list1 + [1, 5, 77]
print(list1)

# 수정 --> 인덱스를 찾아서 대입

list1[3] = 40
print(list1)

# 삭제 --> 인덱스로 찾아서 삭제, del 키워드 이용

del list1[4]
print(list1)

# list의 핵심은 index를 잘 찾는 것.

# 리스트의 길이 구하기 -->  len() 함수
print(len(list1))



# 복습

# n과 m 사이의 수 중 k의 배수 출력
n = 10
m = 30
k = 3

# 추가
list1 = []

list1 = list1 + ["pizza", "마라탕"]

print(list1)

list1[1]="옥수수소시지"
    
print(list1)