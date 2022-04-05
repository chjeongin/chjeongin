






user1 = {"아이디" : "hong123", "비밀번호" : "1234", "이름" : "홍길동"}
user2 = {"아이디" : "song7", "비밀번호" : "7777", "이름" : "손흥민"}
user3 = {"아이디" : "ryu99", "비밀번호" : "9999", "이름" : "류현진"}

# user_keys = ["아이디", "비밀번호", "이름"]
user_list = [user1, user2, user3]
user_keys = user1.keys()

for user in user_list : 
    for key in user_keys : 
        print("{} : {}".format(key, user[key]))
    print("================")
    

# print("아이디 : {}".format(user1["아이디"]))
# print("비밀번호 : {}".format(user1["비밀번호"]))
# print("이름 : {}".format(user1["이름"]))

# list7에 있는 전체
