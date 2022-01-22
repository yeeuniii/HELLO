'''
## 예제 5.1
print("Enter your name.")
name = input()
print("Hello. My name is ",name)

##
name = input("Enter your name:")

## 예제 5.2
print("My"),
print("name"),
print("is"),
print("yeeun.")

print("My","name","is","")

## 예제 5.3
f = float(input("fahrenheit temperature : "))
c = 5.0/9*(f-32)
print(c)


## 예제 5.4 (왜 안될까?!)
import urllib.request
file = urllib.request.urlopen("http://helloworldbbook.com/data/message.txt")
message = file.read()
print(message)
'''

### 도전하기
# 1
first = "yeeun"
second = "park"
print("Hi. I`m",second+first)

# 2
first_name = input("Enter your first name : ")
second_name = input("Enter your second name : ")
print(second_name+first_name)

# 3
length = float(input("사각형 방의 가로의 길이가 몇입니까?"))
high = float(input("사각형 방의 세로의 길이가 몇입니까?"))
print("사각형 방의 넓이는 ", length*high, "피트입니다.")

# 5
a = int(input("500원짜리가 몇 개 있나요?"))
b = int(input("100원짜리가 몇 개 있나요?"))
c = int(input("50원짜리가 몇 개 있나요?"))
d = int(input("10원짜리가 몇 개 있나요?"))
print("잔돈의 총합은 ",a*500+b*100+c*50+d*10, "원입니다.")
