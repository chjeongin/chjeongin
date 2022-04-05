# list7에 있는 전체 회원 정보를 출력해 주세요. 

list7 = [ 
          {"이름" : "홍길동", "거주지" : "대전", "나이" : 23}
         ,{"이름" : "이순신", "거주지" : "서울", "나이" : 36}
         ,{"이름" : "임꺽정", "거주지" : "울산", "나이" : 44}
        ]

user1 = list7[0]

# user_keys = ["이름", "거주지", "나이"]
user_keys = user1.keys()

for user in list7 : 
    for key in user_keys :
        print(user[key])
        

    