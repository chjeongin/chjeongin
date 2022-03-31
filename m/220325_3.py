
# 사람 2명 만들어서 자기소개하기 

# 한사람의 정보는 고향, 나이, 이름 3개로 이루어져있다.


# 자기소개 함수 작성
def introduce(person):
    print("{}사는 {}살의 {}입니다.".format(person[0],person[1],person[2]))


# 대전, 20, 홍길동
# age = 20
# home = "대전"
# name = "홍길동"

hong = ["대전",20,"홍길동"]

introduce(hong)

# 서울, 21, 이순신
age1 = 21
home1 = "서울"
name1 = "이순신"

# 리스트 ==> 일괄처리

# dictionary = { key : 값} ==> 데이터 구조화

def introduce(person):
    print("{}사는 {}살의 {}입니다.".format(person["home"],person["age"],person["name"]))


hong = {"age" : 23, "name" : "홍길동", "home" : "대전"}

lee = {"age" : 21, "name" : "이순신", "home" : "서울"}

introduce(lee)
# print(hong)
# print(hong["age"])

print("=============================================")

# 딕셔너리  CRUD

# 1. 선언
# 리스트
list1=[]
# 딕셔너리
dict1={}

# 2. 추가
# 리스트
list1.append(10)
list1.append(55)
# 딕셔너리 ==> 딕셔너리이름[ "key" ] = value
dict1["food"]= "마라탕"
print(dict1)

# 3. 조회
# 리스트
print(list1[0]) #인덱스로 조회
# 딕셔너리
print(dict1["food"]) #키로 조회

# 4. 수정
dict1["food"]= "마라탕"
dict1["favorite"]= "마라탕" #키가 존재하면 수정, 없으면 추가로 수행


# 5. 삭제
del list1[0]
print(list1)

del dict1["food"]
print(dict1)

#  6. 기타
dict1["food"]= "마라탕"
dict1["char"]= "chunsic"
print(dict1.keys())
print(dict1.values())

for key in dict1.keys() :
    print(dict1[key])
    
    

    