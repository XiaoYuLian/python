import pygame,sys#sys负责控制环境变量，sys.out控制退出

pygame.init()#对pygame内部各模块进行初始化创建和设置
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("pygame 教程")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
    pygame.display.update