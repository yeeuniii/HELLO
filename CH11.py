# 예제 11.1
print("곱셈표")
for i in range(5,8):
    print("\n")
    print(i, "단")
    for j in range(1,10):
        print(i, "x", j, "=", i*j)

##
stars = int(input("How many stars do you want? "))
for i in range(stars):
    print("*", end="")

# 예제 11.2
lines = int(input("How many lines of stars do you want?"))
stars = int(input("How many stars per line? "))
for i in range(lines):
    for j in range(stars):
        print("*", end="")
    print("")   # 다음줄로

# 예제 11.3
blocks = int(input("How many blocks of stars do you want? "))
lines = int(input("How many lines in each block "))
stars = int(input("How many stars per line? "))
for i in range(blocks):
    for j in range(lines):
        for k in range(stars):
            print("*", end="")
        print()
    print()

# 예제 11.4
blocks = int(input("How many blocks of stars do you want? "))
for i in range(1, blocks+1):
    for j in range(1, i*2):
        for k in range(1, (i+j)*2):
            print("*", end="")
        print("")
    print("")

# 예제 11.5
blocks = int(input("How many blocks of stars do you want? "))
for i in range(1, blocks+1):
    print("block =", i)
    for j in range(1, i*2):
        for k in range(1, (i+j)*2):
            print("*", end="")
        print(" line =", j, "star=", k)
    print()

# 예제 11.6 & 11.7
print("\t\tDog\tBun \tKetchup\tMustard\tOnions\tCalories")
dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40
count = 1
for i in [0, 1]:
    for j in [0, 1]:
        for k in [0, 1]:
            for m in [0, 1]:
                for n in [0, 1]:
                    whole_cal = dog_cal*i+bun_cal*j+ket_cal*k+mus_cal*m+onion_cal*n
                    print("#", count, "\t", end="")
                    print(i, "\t", j, "  \t", k, "\t\t", m, "\t\t", n, "\t\t", whole_cal)
                    count = count+1

# 도전하기
# 1
import time
sec = int(input("Countdown timer: How many seconds? "))
for i in range(sec, 0, -1):
    print(i)
    time.sleep(1)
print("BLAST OFF!!")

# 2
sec = int(input("Countdown timer: How many seconds? "))
for i in range(sec, 0, -1):
    print(i, end=" ")        # print(i, "*"*i)
    for j in range(i):
        print("*", end=" ")
    print()
    time.sleep(1)
print("BLAST OFF!!")