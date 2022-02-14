import pygame,sys

size = width , heigh = 600,400
speed = [1,1]
black = 0,0,0
screen = pygame.display.set_mode(size)
pygame.display.srt_caption("pygame碰撞小球")
ball = pygame.image.load()#载入笑傲求的图像，支持jpg，png和gif（非动画）等格式
'''pygame使用内部定义的surface对象表示所有载入的图像
   其中.get_rect()方法获得一个覆盖图像的外接矩形图像
   rect对象有一些重要属性：上下左右宽高等(top,bottom,left,right,width,height)
'''
ballrect = ball.get_rect()


while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0],speed[1])
    if (ballrect.left < 0 or ballrect.right > width):
        speed[0]=-speed[0]
    if (ballrect.top > 0 or ballrect.bottom > heigh):
        speed[1]=-speed[1]
'''ballrect.move(a,b)-->矩形移动一个偏移量a,b为整数'''        

screen.fill(black)#填充背景颜色
screen.blit(ball,ballrect)#将ball绘制在ballrect上
'''由于之前控制的是矩形框在移动，
所以我们需要不断地将图像绘制在矩形框之中来实现小球的移动'''
pygame.display.update()
