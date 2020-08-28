import pygame


from plan_sprites import *


pygame.init()
print("游戏开始。。。。")

# print("英雄的位置 %d %d "%(hero_rect.x,hero_rect.y))
# print("英雄的尺寸 %d %d "%(hero_rect.width,hero_rect.height))
# 绘制
scree = pygame.display.set_mode((480,700))
# 加载背景图像
bg=pygame.image.load("./images/background.png")
# bilt绘制图像
scree.blit(bg,(0,0))
# update更新图像
# pygame.display.update()
# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")

#scree.blit(hero,(100,500))
# 可以绘制全部完成后统一调用update
pygame.display.update()

i = 0
# 创建个时钟对象
clock = pygame.time.Clock()
hero_rect = pygame.Rect(150,300,102,126)
# 创建敌机的精灵
enemy = GameSprites("./images/enemy1.png")
enemy1 = GameSprites("./images/enemy2.png",2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)
    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:

        print(event_list)


    for event in event_list:
        if event.type == pygame.QUIT:
            print("游戏退出。。。")
            # 调用 quit卸载所有模块
            pygame.quit()
            # 退出游戏
            exit()
    # 英雄移动的距离
    hero_rect.y -=1
    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y =700
    # bilt绘制图像
    scree.blit(bg,(0,0)) # 绘制背景图像覆盖上次的图像
    scree.blit(hero,hero_rect)
    # 让精灵组调用两个方法
    # update

    enemy_group.update()

    # draw
    enemy_group.draw(scree)
    # 更新图像
    pygame.display.update()
    # 创建游戏的窗口



pygame.quit()