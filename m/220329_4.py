# list7에 있는 전체 회원 정보를 출력해 주세요. 

list1 = [ 
          {"이름" : "홍길동", "거주지" : "대전", "나이" : 23}
         ,{"이름" : "이순신", "거주지" : "서울", "나이" : 36}
         ,{"이름" : "임꺽정", "거주지" : "울산", "나이" : 44}
        ]

user1 = list1[0]
print(user1)

user_keys = user1.keys()
print(user_keys)

for user in list1:
    for key in user_keys:
        print (user[key])
    print("========")
        
# hong123 아이디를 가진 회원의 이름 출력 
# 출력 : 홍길동

for i 
