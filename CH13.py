# 예제 13.1
def printMyAdderess():
    print("Warren Sande \n123 Main Street \nOttawa, Ontario, Canada \nK2M 2E9")
    print()

printMyAdderess()

# 예제 13.2
def printMyAdderess(myName):
    print(myName, "\n123 Main Street \nOttawa, Ontario, Canada \nK2M 2E9")
    print()

printMyAdderess("Yeeun")

# 예제 13.3
def printMyAdderess(someName, houseNum):
    print(someName, "\n"+houseNum, "Main Street \nOttawa, Ontario, Canada \nK2M 2E9")
    print()

printMyAdderess("Yeeun", "123")

##
def calculateTax(price, tax_rate):
    taxTotal = price + (price * tax_rate)
    return taxTotal

totalPrice = calculateTax(7.99, 0.06)
print(totalPrice)

# 예제 13.4 - 6
def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    print(my_price)
    return total

my_price = float(input("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)
print("price =", my_price, "Total price =", totalPrice)
# print(price)

# 예제 13.7
def calculateTax(price, tax_rate):
    total = price * (1+tax_rate)
    my_price = 10000
    print("my_price (inside function) =", my_price)
    return total

my_price = float(input("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)
print("price =", my_price, "Total price =", totalPrice)
print("my_price (outside function) =", my_price)


# 도전하기
# 1
def drawmyname():
    print("Y     Y  EEEEEE  EEEEEE  U     U  N     N")
    print(" Y   Y   E       E       U     U  NN    N")
    print("  Y Y    EEEE    EEEE    U     U  N N   N")
    print("   Y     E       E        U   U   N  N  N")
    print("   Y     E       E        U   U   N   N N")
    print("   Y     EEEEEE  EEEEEE    UUU    N    NN")

drawmyname()

for i in range(5):
    drawmyname()

# 2
def pers_inf(name, address, house_num, si, do, zip_code, country):
    print("Name:", name)
    print("Address:", address)
    print("House number:", house_num)
    print(country, do+"도", si+"시", zip_code)

# pers_inf("박예은", "광교호반마을", "21단지", "수원", "경기", "16513", "대한민국")

pers_list = []
pers_list.append(input("이름: "))
pers_list.append(input("주소: "))
pers_list.append(input("번지: "))
pers_list.append(input("시: "))
pers_list.append(input("도: "))
pers_list.append(input("우편번호: "))
pers_list.append(input("나라: "))

def pers_inff(list):
    print("Name:", list[0])
    print(list[6], list[4] + "도", list[3] + "시")
    print(list[1], list[2])
    print("Zip Code: ", list[5])

pers_inff(pers_list)

# 3
def calculateTax(price, tax_rate):
    global my_price
    my_price = 10000
    total = price * (1 + tax_rate)
    print("my_price (inside function) =", my_price)
    return total

my_price = float(input("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)
print("price =", my_price, "Total price =", totalPrice)
print("my_price (outside function) =", my_price)

# 4
def TotalMoney(num500, num100, num50, num10):
    total = num500*500+num100*100+num50*50+num10*10
    return total

num500 = int(input("500원짜리가 몇 개 있나요?"))
num100 = int(input("100원짜리가 몇 개 있나요?"))
num50 = int(input("50원짜리가 몇 개 있나요?"))
num10 = int(input("10원짜리가 몇 개 있나요?"))
total = TotalMoney(num500, num100, num50, num10)

print("500won:", str(num500),
      "\n100won:", str(num100),
      "\n50won:", str(num50),
      "\n10won:", str(num10),
      "\ntotal is", str(total)+"won")
