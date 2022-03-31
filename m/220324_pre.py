# n과 m 사이의 수 중 k의 배수 출력
n = 10
m = 30
k = 3

# a = n
# end = m
# while a <= end :
    

#     print(a)
#     a += k

start = n
end = m
# n과 m사이의 k배수 (ex k=3, 12,15,18...)


# n이상부터 시작하는 s

while start <= end :
    if start % k == 0 :
        print(start)
    start += 1
    