user1 = {"아이디" : "hong123", "비밀번호" : "1234", "이름" : "홍길동"}
user2 = {"아이디" : "song7", "비밀번호" : "7777", "이름" : "손흥민"}
user3 = {"아이디" : "ryu99", "비밀번호" : "9999", "이름" : "류현진"}

# 아이디를 넘기면 그 아이디에 해당하는 회원 딕셔너리 알아보기
user_list = [user1, user2, user3]
user_keys = user1.keys()

def get_user_by_id(id) :
    for user in user_list :
        if user["아이디"] == id :
            return user
        
def print_all_userid() :
    for user in user_list :
        



# hong123 아이디를 가진 회원의 이름 출력
# 출력 : 홍길동

for user in user_list :
    if user["아이디"] == "hong123":
        print(user["이름"])
        
# hong123 아이디를 가진 회원의 비밀번호를 3333으로 수정 후 모든 회원 정보 출력
# 출력 : 3333

for user in user_list:
    if user["아이디"] == "hong123" : 
        user["비밀번호"] = 3333

for user in user_list:
    if user["아이디"] == "hong123" : 
        print(user_list)
        
# 
user1 = get_user_by_id("hong123")
print(user1["이름"])
print(user1["비밀번호"])


user2 = get_user_by_id("hong123")
user2["비밀번호"] = 3333
print(user1["비밀번호"])

cha = {"아이디" : "chacha", "이름", : "차태진", "비밀번호" : "c123"}
user_list.append(cha)

hong = {"아이디" : "hong123", "이름", : "홍길순", "비밀번호" : "h1234"}
user = get user_by_id("hong1234")

if user != None : 
    print("이미 존재하는 회원입니다")
else : 
    user_list.append(hong)
    
print("==================")
print_all_userid()



print_all_userid()

# 모든 회원 아이디를 출력
for user in user_list :
    print(user["아이디"])


    
