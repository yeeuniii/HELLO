# 예제 7.1
num1 = int(input("Enter the first number."))
num2 = int(input("Enter the second number."))
if num1 == num2:
    print(num1, "is equal to", num2)
if num1 != num2:
    print(num1, "is not equal to", num2)
if num1 > num2:
    print(num1, "is greater than", num2)
if num1 < num2:
    print(num1, "is less than", num2)

##
answer = int(input("Enter the integer number among 1~15."))
if answer >= 10:
    print("You got at least 10!")
elif answer >= 5:
    print("You got at least 5!")
elif answer >= 3:
    print("You got at least 3!")
else:
    print("You got less than 3.")


## 8살 이상 & 최소한 3학년 을 위한 게임
age = int(input("나이를 입력하시오."))
grade = int(input("학년을 입력하시오."))

# WAY 1
if age >= 8 and grade >= 3:
    print("게임을 실행할 수 있습니다.")
else:
    print("3학년, 8살 이상부터 게임을 실행할 수 있습니다.")

# WAY 2
if age >= 8:
    if grade >= 3:
        print('You can do this game!')
else:
    print("Sorry. You`re not right age to do this game")


# 도전하기
# 1
price = int(input("물건의 가격이 얼마입니까?"))
if price <= 100000:
    price = price*(1-0.1)
    print("상품 할인율은 10%입니다. \n 물건의 최종 가격은", price, "원 입니다.")
else:
    price = price*(1-0.2)
    print("상품 할인율은 20%입니다. \n 물건의 최종 가격은", price, "원 입니다.")

# 2
import easygui
sex = easygui.choicebox("성별을 고르시오. \n 단, 여자는 f, 남자는 m", choices=["f","m"])
age = int(input("나이를 입력하시오."))
if sex == "f" and (10 <= age <= 12):
    print("축구팀에서 뛸 수 있습니다.")
else:
    print("조건에 부합하지 않습니다.")

# 보너스(사용자가 여자가 아니라면 나이를 묻지 않도록.)
sex = input("성별을 고르시오. \n 단, 여자는 f, 남자는 m")
if sex == "f":
    age = int(input("나이를 입력하시오."))
    if 10 <= age <= 12:
        print("축구팀에서 뛸 수 있습니다.")
    else:
        print("적합한 나이가 아닙니다.")
else:
    print("여자만 축구팀에서 뛸 수 있습니다.")

# 3
size = int(input("휘발유 탱크의 크기가 몇 리터입니까?\n"))
percent = int(input("휘발유 탱크는 현재 얼마나 차 있습니까? \n(%로 나타낼 것. 예를 들어, 반이 차 있으면 50%)\n"))
km = int(input("여러분의 차는 휘발유 1리터에 몇 킬로미터 갑니까?\n"))
go = (size-5)*(percent/100)*km
print("Size of tank:", size,
      "\npercent full:", percent,
      "\nkm per liter:", km,
      "\nYou can go another", go, "km",
      "\nThe next gas station is 200 km away")
if go >= 200:
    print("You can wait for the next station.")
else:
    print("Get gas now!")

# 4
password = "0913"
answer = input("비밀번호를 입력하시오.")
if answer == password:
    print("통과되었습니다.")
else:
    print("올바른 비밀번호가 아닙니다.")