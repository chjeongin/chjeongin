# 경로 -> .의 의미 : 자기 자신이 있는 폴더
from pybo import db


# --------------------------------------
# 사람 --> 이름, 나이, 성별

class Person(db.model) :
    # 자료형 => 길이가 있는 문자, 길이가 없는 문자, 숫자, 날짜
    # 사람을 식별할 번호
    no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30)) #String(길이) - 길이 있는 문자
    age = db.Column(db.Integer) #Integer -> 숫자
    gender = db.Column(db.String(10))
    
    
    # def __init__(self, name, age, address) :
    #     self.name = name
    #     self.age = age
    #     self.address = address


# p1 = Person("Chunsic", 1, "서울")        

# print(p1.name)
