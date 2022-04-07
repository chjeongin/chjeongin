# 1
item1 = {"품목" : "바나나", "가격" : 5000,  "수량" : 1, "날짜" : "2021.08월 5일"}
item2 = {"품목" : "커피"  , "가격" : 3000,  "수량" : 2, "날짜" : "2021년 08월 5일"}
item3 = {"품목" : "책"    , "가격" : 15000, "수량" : 1, "날짜" : "2021년 08월 6일"}
item4 = {"품목" : "펜"    , "가격" : 2000,  "수량" : 4, "날짜" : "2021년 08월 6일"}

items = [item1,item2,item3,item4]
header = ["품목", "가격", "수량", "날짜"]


from openpyxl import Workbook

wb = Workbook()


ws1 = wb.active
ws1.title = "Orders"
ws1 = wb["Orders"]

ws1.append(["품목", "가격", "수량", "날짜"])




for item in items :
    values = item.values()
    values = list(values)
    ws1.append(values)
    



wb.save("test2.xlsx")




