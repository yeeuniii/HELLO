# 예제 14.1 & 2
class Ball:     # 클래스 생성 ; 객체의 정의

    def bounce(self):   # 메서드 정의
        if self.direction == "down":
            self.direction ="up"

myBall = Ball()     # 인스턴스 생성
myBall.direction = "down"   # 속성 정의
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

# 예제 14.3
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