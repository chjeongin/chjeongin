import math as m

# print(m.ceil(99.55))
print(m.sqrt(5))
# . ==> 연산자 (멤버 접근 연산자)

print("-"*50)



car1 = {"모델" : "싼타페", "가격": 3000, "색상": "red"}





class Car :

    def __init__(self, model, price, color) :
        self.model = model
        self.price = price
        self.color = color
    def drive(self) :
        print("가격은 {}, {}색 {}가 주행중입니다.".format(self.price,self.color,self.model))



c1 = Car("아반떼", "하얀", 1000) #복제본을 하나 만들어줌.
c2 = Car(2000,"하얀","아반떼")
c3 = Car("하얀",2000,"아반떼")
c1.drive()
c2.drive()
c3.drive()
# c2 = Car()

# c3 = Car()



# 클래스와 객체를 사용하는 이유
# 1. 관련있는 것(데이터 및 함수)끼리 묶어서 효율적으로 관리
# 2. 사람이 인식하는 방식과 비슷 
# ==> 세상 모든 것은 상태와 동장, 그것을 행하는 주체.
# ==> 돌맹이 : -색, 크기, 모양, -굴러가다, 깨지다
# 3. 상태 - > 변수, 동작 -> 함수 ==> 두개 묶으면 주체(사물, 객체)


