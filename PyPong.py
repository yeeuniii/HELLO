import pygame
import sys
import random
import os
os.chdir("C:/Users/박예은/AppData/Local/Programs/Python/Python37/One_Big_Archive/PyPong")


class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        global points, score_text
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0] + random.randint(-3, 3)

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1] + random.randint(-3, 3)
            points = points + 1
            score_text = font.render(str(points), True, [0, 0, 0])


class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])   # 표면 생성
        image_surface.fill([0, 0, 0])
        self.image = image_surface.convert()    # 표면 => 이미지 변환
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
ball_speed = [10, 5]
my_ball = MyBallClass("wackyball.bmp", ball_speed, [50, 50])
ballgroup = pygame.sprite.Group(my_ball)
paddle = MyPaddleClass([270, 400])
clock = pygame.time.Clock()
lives = 3
points = 0

font = pygame.font.Font(None, 50)
score_text = font.render(str(points), True, (0, 0, 0))
textpos = [10, 10]
done = False

while 1:
    clock.tick(30)
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 마우스로 패들 조종
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(paddle, ballgroup, False):
        my_ball.speed[0] = my_ball.speed[0] + random.randint(-3, 3)
        my_ball.speed[1] = -my_ball.speed[1] + random.randint(-3, 3)
    my_ball.move()

    if 0 < my_ball.speed[0] < 3:
        my_ball.speed[0] = 3
    if -3 < my_ball.speed[0] <= 0:
        my_ball.speed[0] = -3
    if my_ball.speed[0] > 15:
        my_ball.speed[0] = 15
    if 0 < my_ball.speed[1] < 3:
        my_ball.speed[1] = 3
    if -3 < my_ball.speed[1] <= 0:
        my_ball.speed[1] = -3
    if my_ball.speed[1] > 15:
        my_ball.speed[1] = 15

    if not done:
        screen.blit(my_ball.image, my_ball.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_text, textpos)
        for i in range(lives):
            width = screen.get_rect().width
            screen.blit(my_ball.image, [width - 40 * i, 20])
        pygame.display.flip()

    if my_ball.rect.top >= screen.get_height():
        lives = lives - 1

        if lives == 0:
            final_text1 = "GAME OVER"
            final_text2 = "You`r final score is " + str(points)
            ft1_font = pygame.font.Font(None, 70)
            ft1 = ft1_font.render(final_text1, True, [0, 0, 0])
            ft2_font = pygame.font.Font(None, 50)
            ft2 = ft2_font.render(final_text2, True, [0, 0, 0])
            screen.blit(ft1, [(screen.get_width()-ft2.get_width())/2, 100])
            screen.blit(ft2, [(screen.get_width()-ft2.get_width())/2, 200])
            pygame.display.flip()
            done = True

        else:
            pygame.time.delay(2000)
            my_ball.rect.topleft = [screen.get_width() - 40*lives, 50]
