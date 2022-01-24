# 예제 8.1
for i in [1, 2, 3, 4, 5]:
    print("hello")

# 예제 8.2
for i in [1, 2, 3, 4, 5]:
    print(i)

# 예제 8.3
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i, "times 8 =", i * 8)

# 예제 8.4
for i in range(1, 10):
    print(i, "times 8 =", i * 8)

##
for i in range(1, 10, 2):
    print(i)
for i in range(5, 26, 5):
    print(i)
for i in range(10, 0, -1):
    print(i)

# 예제 8.6
# 카운트다운 타이머
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("BLAST OFF!!")

# 예제 8.7
for i in ["Spongebob", "Spiderman", "Justin Timberlake", "My dad"]:
    print(i, "is the coolest guy ever!")

# 예제 8.8
print("Type 3 to continue, anything else to quit.")
some = input()
while some == "3":
    print("Thank you for the 3. Very kind of you\n"
          "Type 3 to continue, anything else to quit.")
    some = input()
print("That`s not 3, I`m quitting now")

# 예제 8.9
for i in range(1, 6):
    print()
    print("i =", i)
    print("Hello, how")
    if i == 3:
        continue
    print("are you today?")

for i in range(1, 6):
    print()
    print("i =", i)
    print("Hello, how")
    if i == 3:
        break
    print("are you today?")

# 도전하기
# 1
num = int(input("Which multiplication table would you like?\n"))
print("Here`s your table:")
for i in range(1, 11):
    print(num, "x", i, "=", num*i)

# 2
num = int(input("Which multiplication table would you like?\n"))
print("Here`s your table:")
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i = i+1

# 3
num = int(input("Which multiplication table would you like?\n"))
end = int(input("How high do you want to do?\n"))
print("Here`s your table:")
for i in range(1, end+1):
    print(num, "x", i, "=", num*i)
