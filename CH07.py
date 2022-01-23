"""
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
sex = input('성별을 입력하세요. \n 단, 여자는 f, 남자는 m \n')
age = int(input("나이를 입력하시오."))

if sex == "f" and (10 <= age <= 12):
    print("축구팀에서 뛸 수 있습니다.")
else:
    print("조건에 부합하지 않습니다.")
"""
# 보너스
import easygui
sex = easygui.choicebox("성별을 고르시오. \n 단, 여자는 f, 남자는 m", choices=["f","m"])
if sex == "f":
    age = int(input("나이를 입력하시오."))
elif 10 <= age <= 12:
    print("축구팀에서 뛸 수 있습니다.")
else:
    print("조건에 부합하지 않습니다.")