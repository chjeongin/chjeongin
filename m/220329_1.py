list1 = [[1]]
list2 = [1]

print(list1[0])
print(list2[0])
list3 = [1,2,3]
list4 = [4,5,6]
list5 = [7,8,9]
list6 = [list3, list4, list5]

print(list6[0])
print(list6[1])
print(list6[2])

list7 = list6[1]
print(list7[0])
print(list6[1][0])

# 이중리스트 전체 탐색
# 첫번째행 잡고 모든 열 탐색
# 두번째행 잡고 모든 열 탐색
# 세번째행 잡고 모든 열 탐색

# 행렬 전체 탐색
list3 = [1,2,3]
list4 = [4,5,6]
list5 = [7,8,9]
list6 = [list3, list4, list5]
# list7 = [[1,2,3],[4,5,6],[7,8,9]]
list7 = [
        {"이름" : "홍길동", "거주지" : "대전", "나이" : 23}, 
        {"이름" : "이순신", "거주지" : "서울", "나이" : 36}, 
        {"이름" : "임꺽정", "거주지" : "울산", "나이" : 44}, 
        ]

for row in list7 :
    for col in row :
        print(col, end = " ") 
    print()
    


# print("{} {} {}".format(list7[0][0], list7[0][1], list7[0][2]))
# print("{} {} {}".format(list7[1][0], list7[1][1], list7[1][2]))
# print("{} {} {}".format(list7[2][0], list7[2][1], list7[2][2]))

# print("{} {} {}".format(list7[i][0], list7[i][1], list7[i][2]))

# for i in range(0, 3, 1):
#     row = list7[i]
#     for j in range(0, 3, 1):
#         print(row[j], end = " ")
#     print()
        
        







