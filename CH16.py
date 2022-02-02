# 예제 16.1 - 2
import pygame, sys
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
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
for i in range(100):
    width = random.randint(0,250)
    height = random.randint(0, 100)
    top = random.randint(0,400)
    left = random.randint(0, 500)
    color_name = random.choice(THECOLORS.keys())
    color = THECOLORS[color_name]
    line_width = random.randint(1, 3)
    pygame.draw.rect(screen, color, [left, top, width, height], line_width)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
