# 예제 15.2
import my_module

celsius = int(input("Enter a temperature in Celsius: "))
fahrenheit = my_module.c_to_f(celsius)
print("That`s", fahrenheit, "degrees Fahrenheit")

# 예제 15.3 (time module)
import time
print("How", end=" ")
time.sleep(1)
print("are", end=" ")
time.sleep(1)
print("you", end=" ")
time.sleep(1)
print("today?")

##
from time import sleep
print("How", end=" ")
sleep(1)
print("are", end=" ")
sleep(1)
print("you", end=" ")
sleep(1)
print("today?")

# random module
import random
for i in range(3):
    print(random.randint(0, 100))
for i in range(3):
    print(random.random())
for i in range(3):
    print(random.random()*10)


# 도전하기
# 1
from printmyname import printmyname
printmyname()

## 이건 왜 결과가 이래?
# import CH13
# CH13.printmyname()

# 2
from my_module import c_to_f
celsius = int(input("Enter a temperature in Celsius: "))
fahrenheit = c_to_f(celsius)
print("That`s", fahrenheit, "degrees Fahrenheit")

# 3
import random
for i in range(5):
    print(random.randint(1,20))

# 4
import random
import time

count = 0
while count < 30:
    print(count, "sec")
    print(random.random())
    time.sleep(3)
    count = count + 3
