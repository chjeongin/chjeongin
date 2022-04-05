list1 = [1,2,3,4,5,6,7,8,9,10]

# for 반복문 ==> 리스트에 특화된 반복문
for num in list1 :
    print(num, end = ' ')

# 홀수번째만 출력
# 수열리스트를 만드는 함수 range()
# 1부터 10의 홀수
# range(시작, 끝 +1, 증가량)
print("\n")
print(list(range(1,11,2)))

for num in range(1,11,2) :
    print(num)
    
# 구구단

for dan in range(2, 10, 1) :
    print("==={}단===".format(dan))
    for i in range(1,9,1) :
        print("{} * {} = {}".format(dan, i, dan*i))
    
