list1=[1,55,66,99,77,33,]
list2=["a","b","c","d","e"]


def print_list(x) :
    for num in x :
        print(num)
    

# 함수호출
# print_list(list1)
# print_list(list2)

# return --> 함수의 종료, 본래의 자리로 돌아가서 실행
# 원의 넓이를 구하라
# 반지름*반지름*(3.14)
def cir_area(r) :
    return r * r * 3.14
    
# r=5
cir_area(5)
# r=10
cir_area(10)
# r=3
cir_area(3)

# 반지름 4인 원 넓이의 2배값은?
print(cir_area(4)*2)

# error 'None' --> 값이 없음을 의미하는 값

# return(반환) -> 함수의 결과값을 받아서 2차 작업을 하기 위해 함수가 값으로 바뀌는 것.


# 자판기함수
def ven_machine(in_money, no) :
    print("현재 투입 금액 : {}원".format(in_money))
    
    
    beverages = ["사이다", "콜라", "커피", "생수"]
    prices = [1000,1200,800,700]
    if prices[no] > in_money :
        print("잔액이 부족합니다.")
        return
    print("잔액은 {}원".format(in_money-prices[no]))
    return beverages[no]


# 0 사이다, 1 콜라, 2 커피, 3 생수
result = ven_machine(1000,0)
print(result)

result = ven_machine(1000,1)
print(result)





