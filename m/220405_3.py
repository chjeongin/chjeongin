# 다음 코드가 동작하도록 class를 완성해주세요

class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        
        
    
    def introduce(self) :
        print("안녕하세요. {}살 {}입니다.".format(self.age, self.name))


class Car :
    def __init__(self,model,color,vel ) :
        self.model = model
        self.color = color
        self.vel = vel
    def drive(self) :
        print("{} {}이/가 {}km로 달립니다.".format(self.color, self.model, self.vel))
        

class Cat :
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed 
        self.age = age
    def meow(self) :
        print("{}살 {} {}가 야옹하고 웁니다.".format(self.age, self.breed, self.name))
        
class Warrior :
    def __init__(self, name, att, defend) :
        self.name = name
        self.att = att
        self.defend = defend
    def status(self) :
        print("이름 : {}, 공격력 : {}, 방어력 : {}".format(self.name, self.att, self.defend))
        
    def attack(self) :
        print("{}이 {}의 데미지를 입힙니다.".format(self.name, self.att))
    def defense(self) :
        print("{}이 {} 데미지를 방어합니다.".format(self.name,self.defend))
        
        

p1 = Person("홍길동", 27)
p2 = Person("홍길순", 25)

p1.introduce() # 안녕하세요 27살 홍길동입니다.
p2.introduce() # 안녕하세요 25살 홍길순입니다.

c1 = Car("소나타", "하얀색", 100)
c2 = Car("모닝", "검정색", 70)

c1.drive() # 하얀색 소나타이/가 100km로 달립니다.
c2.drive() # 검정색 모닝이/가 70km로 달립니다.

cat1 = Cat("아리", "러시안블루", 4)
cat2 = Cat("망고", "샴", 6)

cat1.meow() # 4살 러시안블루 고양이 아리가 야옹하고 웁니다.
cat2.meow() # 6살 샴 고양이 망고가 야옹하고 웁니다.

w1 = Warrior("이순신", 20, 10)
w2 = Warrior("강감찬", 15, 15)

w1.status() # 이름 : 이순신, 공격력 : 20, 방어력 : 10 
w2.status() # 이름 : 강감찬, 공격력 : 15, 방어력 : 15 

w1.attack() # 이순신이 20의 데미지를 입힙민다.
w2.attack() # 강감찬이 15의 데미지를 입힙민다. 

w1.defense() # 이순신이 10 데미지를 방어합니다.
w2.defense() # 강감찬이 15 데미지를 방어합니다.

