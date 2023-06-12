import pygame
import sys
import random

#  初始化
pygame.init()
screen = pygame.display.set_mode((900, 700))
clock = pygame.time.Clock()
FPS = 60

#  加载图片
bg = pygame.image.load('pic/bg.png')

#  金币类
class  Gold:
    def __init__(self):
        self.image = pygame.image.load('pic/gold.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 860)
        self.rect.y = random.randint(700, 900)

    def draw(self):
        screen.blit(self.image, self.rect)
        
    #——————————————————————————————————————————————————————
    def move(self):
        self.rect.y -= 1
        #【你需要在这里判断金币是否移出边界】
        if self.rect.y <= 0:
            self.rect.x = random.randint(0, 860)
            self.rect.y = random.randint(700, 900)            

    #------------------------------------------------------

# 生成金币对象
gold1 = Gold()
gold2 = Gold()


#  主循环模块
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 绘制背景
    screen.blit(bg, (0, 0))
    
    # 绘制金币
    gold1.draw()
    gold2.draw()

    # 金币移动
    gold1.move()
    gold2.move()

    pygame.display.update()
    clock.tick(FPS)

