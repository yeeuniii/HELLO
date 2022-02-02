# 예제 16.1 - 2
import pygame
pygame.init()
screen = pygame.display.set_mode([640, 380])
while True:
    pass

# 예제 16.3 - 4
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 380])    # 화면표시객체 ; [폭, 높이]
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [255, 0, 0], [100, 100], 30, 0)      #
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# 예제 16.5
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 380])
screen.fill([255, 255, 255])
# pygame.draw.circle(screen, [255, 0, 0], [320, 190], 30, 0)      # circle
pygame.draw.rect(screen, [255, 0, 0], [250, 150, 300, 200], 20)  # 1
# my_list = [250, 150, 300, 200]                                # 2 ; 리스트
# pygame.draw.rect(screen, [255, 0, 0], my_list, 0)
# my_rect = pygame.Rect(250, 150, 300, 200)                     # 3 ; 튜플
# pygame.draw.rect(screen, [255, 0, 0], my_rect, 0)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# 예제 16.6
import pygame, sys, random
from pygame.colordict import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
for i in range(100):
    width = random.randint(0,250)
    height = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)
    color_name = random.choice(list(THECOLORS.keys()))
    color = THECOLORS[color_name]
    line_width = random.randint(1, 3)
    pygame.draw.rect(screen, color, [left, top, width, height], line_width)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# 예제 16.8
import pygame, sys
import math
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
for x in range(0, 640):
    y = int(math.sin(x/640*4*math.pi)*200+240)
    pygame.draw.rect(screen, [0, 0, 0], [x, y, 1, 1], 1)    # 사각형으로
    pygame.draw.circle(screen, [0, 0, 0], [x, y], 1, 1)     # 원으로
#   screen.set_at([x, y], [0, 0, 0])
# screen.set_at([1, int(math.sin(1/640*4*math.pi)*200+240)], [255, 0, 0])
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# 예제 16.9
import pygame, sys
import math
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
points = []
for x in range(0, 640):
    y = int(math.sin(x/640*4*math.pi)*200+240)
    points.append([x, y])
pygame.draw.lines(screen, [0, 0, 0], False, points, 2)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# 예제 16.10
import pygame, sys
pygame.init()

dots = [[221, 432], [225, 331], [133, 342], [141, 310], [51,230],
        [74, 217], [58, 153], [114, 164], [123, 135], [176, 190],
        [159, 77], [193, 93], [230, 28], [267, 93], [301, 77],
        [284, 190], [327, 135], [336, 164], [402, 153], [386, 217],
        [409, 230], [319, 310], [327, 342], [233, 331], [237, 432]]

screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
pygame.draw.lines(screen, [0, 0, 0], True, dots, 2)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# 예제 16.11 - 13
import pygame, sys
import os
os.chdir("C:\\Users\\박예은\\AppData\\Local\\Programs\\Python\\Python37\\One_Big_Archive\\images")
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("beach_ball.png")
screen.blit(my_ball, [50, 50])
pygame.display.flip()
pygame.time.delay(2000)
screen.blit(my_ball, [150, 50])
pygame.draw.rect(screen, [255, 255, 255], [50, 50, 90, 90], 0)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# 예제 16.14 & 15
import pygame
import os
os.chdir("C:\\Users\\박예은\\AppData\\Local\\Programs\\Python\\Python37\\One_Big_Archive\\images")
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
screen.blit(my_ball, [x, y])
pygame.display.flip()
for i in range(1, 200):
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x+5
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

def end():
    import pygame, sys
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

end()

# 예제 16.15 & 16
import pygame, sys
import os
os.chdir("C:\\Users\\박예은\\AppData\\Local\\Programs\\Python\\Python37\\One_Big_Archive\\images")
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
x_speed = 10
y_speed = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 90 or x < 0:
        x_speed = -x_speed
    if y > screen.get_height() - 90 or y < 0:
        y_speed = -y_speed
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

# 예제 16.17
import pygame, sys
import os
os.chdir("C:\\Users\\박예은\\AppData\\Local\\Programs\\Python\\Python37\\One_Big_Archive\\images")
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
x_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x + x_speed
    if x > screen.get_width():
        x = -90
    screen.blit(my_ball, [x, y])
    pygame.display.flip()


# 도전하기
# 1
# import pygame
# help(pygame.draw)

# 2
import pygame, sys
import os
os.chdir("C:\\Users\\박예은\\AppData\\Local\\Programs\\Python\\Python37\\One_Big_Archive\\images")
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
skier_r = pygame.image.load("skier_right2.png")
skier_l = pygame.image.load("skier_left2.png")
x = 50
y = 50
x_speed = 10
screen.blit(skier_r, [50, 50])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(20)

# 4
import pygame, sys
import os
os.chdir("C:\\Users\\박예은\\AppData\\Local\\Programs\\Python\\Python37\\One_Big_Archive\\images")
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
x_speed = 10
y_speed = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() or x < -90:
        x_speed = -x_speed
    if y > screen.get_height() or y < -90:
        y_speed = -y_speed
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

# 5
# 예제 16.6
import pygame, sys, random
from pygame.colordict import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
for i in range(100):
    width = random.randint(0, 250)
    height = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)
    color_name = random.choice(list(THECOLORS.keys()))
    color = THECOLORS[color_name]
    line_width = random.randint(1, 3)
    pygame.draw.rect(screen, color, [left, top, width, height], line_width)
    pygame.display.flip()
    pygame.time.delay(30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
