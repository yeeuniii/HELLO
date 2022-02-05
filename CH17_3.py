import pygame
import sys
import random
import os
os.chdir("C:\\Users\\박예은\\AppData\\Local\\Programs\\Python\\Python37\\One_Big_Archive\\images")


class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)     # call Sprite initializer ; 스프라이트 초기화
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]


def animate(group):
    screen.fill([255, 255, 255])
    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)

        if pygame.sprite.spritecollide(ball, group, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]

        group.add(ball)

        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    pygame.time.delay(20)


size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
img_file = "b_ball_rect.png"
group = pygame.sprite.Group()
for row in range(0, 3):
    for col in range(0, 3):
        location = [col*180+10, row*180+10]
        speed = [random.choice([-2, 2]), random.choice([-2, 2])]
        ball = MyBallClass(img_file, location, speed)
        group.add(ball)     # add the ball to the group

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    animate(group)

