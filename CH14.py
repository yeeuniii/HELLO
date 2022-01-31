# 예제 14.1 & 2 (Ball class)
class Ball:  # 클래스 생성 ; 객체의 정의

    def bounce(self):  # 메서드 정의
        if self.direction == "down":
            self.direction = "up"


myBall = Ball()  # 인스턴스 생성
myBall.direction = "down"  # 속성 정의
myBall.color = "green"
myBall.size = "small"

myBall.bounce()
print("I just created a ball"
      "\nMy ball is", myBall.size,
      "\nMy ball is", myBall.color,
      "\nMy ball`s direction is", myBall.direction,
      "\nNow I`m going to bounce the ball")
print()
myBall.bounce()
print("Now the ball`s direction is", myBall.direction)


# 예제 14.3 (conti.)
class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"


myBall = Ball("red", "small", "down")
print("I just created a ball"
      "\nMy ball is", myBall.size,
      "\nMy ball is", myBall.color,
      "\nMy ball`s direction is", myBall.direction,
      "\nNow I`m going to bounce the ball")
print()
myBall.bounce()
print("Now the ball`s direction is", myBall.direction)

print(myBall)


# 예제 14.4 (conti.)
class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        msg = "Hi, I`m a " + self.size + " " + self.color + " ball!"
        return msg


myBall = Ball("red", "small", "down")
print(myBall)


# 예제 14.5 & 6 (HotDog class)
class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []

    def __str__(self):
        msg = "hot dog"
        if len(self.condiments) > 0:
            msg = msg + " with "
        for i in self.condiments:
            msg = msg + i + ", "
        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + "."
        return msg

    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level > 5:
            self.cooked_string = "Well-done"
        elif self.cooked_level > 3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"

    def add_condiment(self, condiment):
        self.condiments.append(condiment)


myDog = HotDog()

print(myDog.cooked_level)
print(myDog.cooked_string)
print(myDog.condiments)

print("Now I`m going to cook the hot dog")
myDog.cook(4)
print(myDog.cooked_level)
print(myDog.cooked_string)

print(myDog)
print("Cooking hot dog for 4 minutes...")
myDog.cook(4)
print(myDog)
print("Cooking hot dog for 3 more minutes...")
myDog.cook(3)
print(myDog)
print("What happens if I cook it for 10 more minutes?")
myDog.cook(10)
print(myDog)
print("Now, I`m going to add some stuff on my hot dog")
myDog.add_condiment("ketchup")
myDog.add_condiment("mustard")
print(myDog)


##
class GameObject:
    def __init__(self, name):
        self.name = name

    def pickup(self, player):
        pass  # 코드 토막을 만들 때 빈 부분을 채워주는 용도
        # 플레이어의 수집품에 객체를 추가하는 코드


class Coin(GameObject):  # 하위클래스 / 파생클래스
    def __init__(self, value):
        GameObject.__init__(self, "coin")
        self.value = value

    def spend(self, buyer, seller):
        pass
        # 판매자의 돈은 추가되고 구매자의 돈은 감소하는 동전 제거를 위한 코드


# 도전하기
# 1
class BankAccount:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.balance = 0.0

    def showbalance(self):
        print("잔액은", str(self.balance), "원 입니다.")

    def deposit(self, iin):
        print(str(iin) + "원 입금되었습니다.")
        self.balance = self.balance + iin
        print("해당 계좌 잔액은", str(self.balance) + "원 입니다.")

    def withdraw(self, out):
        if out <= self.balance:
            print(str(out) + "원 출금되었습니다.")
            self.balance = self.balance - out
            print("해당 계좌 잔액은", str(self.balance) + "원 입니다.")
        else:
            print("해당 계좌 잔액은", str(self.balance) + "원 입니다.")
            print("출금에 실패하였습니다.")


myAccount = BankAccount("카뱅", 3333)
myAccount.showbalance()
myAccount.deposit(100000)
myAccount.withdraw(50000)
myAccount.withdraw(70000)


# 2
class InterestAccount(BankAccount):
    def __init__(self, name, num, rate):
        BankAccount.__init__(self, name, num)
        self.rate = rate

    def addinterest(self):
        interest = self.balance * self.rate
        self.deposit(interest)
        print("이자는", str(interest) + "원이고, \n잔액은", str(self.balance) + "원입니다.")


myAccount = InterestAccount("카뱅", 3333, 0.06)
print("계좌이름: ", myAccount.name)
print("계좌번호: ", myAccount.num)
print("이자율: ", 100 * myAccount.rate, "%")
myAccount.deposit(100000)
myAccount.addinterest()
