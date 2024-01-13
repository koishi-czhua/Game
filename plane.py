import pygame
import sys
import random

# 初始化pygame
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((800, 600))

# 加载飞机图片
plane_img = pygame.image.load('plane.jpg')
plane_img = pygame.transform.scale(plane_img, (50, 50))

# 飞机的初始位置
plane_position = [200, 500]

#飞机碰撞体积
plane_rect = pygame.Rect(plane_position[0],plane_position[1],50,50)

#飞机生命
plane_live = 3

#判断游戏结束与否
game_over = False

#无敌时间
invincible_time = 0

# 添加一个新的变量来追踪飞机的可见性
plane_visible = True

game_state = "menu"

# 子弹类
class Bullet:
    def __init__(self, position, direction):
        self.img = pygame.image.load('bullet.jpg')  # 加载子弹图片
        self.img = pygame.transform.scale(self.img, (10, 20))  # 调整子弹图片大小
        self.position = position  # 子弹的初始位置
        self.speed = 5  # 子弹的速度
        self.diraction = direction #1↑ -1↓

    def move(self):
        self.position[1] += self.speed * self.diraction  # 更新子弹的位置

    def draw(self):
        screen.blit(self.img, self.position)  # 绘制子弹

# 敌机类
class Enermy:
    def __init__(self):
        self.img = pygame.image.load('enemy.jpg')  # 加载敌机图片
        self.img = pygame.transform.scale(self.img, (50, 50))  # 调整敌机图片大小
        self.reset()

    def reset(self):
        self.position = [random.randint(0, 750), -50]  # 敌机的初始位置
        self.speed = random.randint(1, 3)  # 敌机的速度

    def move(self):
        self.position[1] += self.speed  # 更新敌机的位置
        if self.position[1] > 600:  # 如果敌机飞出屏幕
            self.reset()  # 重置敌机的位置和速度

    def draw(self):
        screen.blit(self.img, self.position)  # 绘制敌机



class Benermy(Enermy):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('benermy.jpg')
        self.img = pygame.transform.scale(self.img, (50, 50))
        self.bullets = []
        self.bullet_frequency = 60
        self.bullet_counter = 0
    
    def move(self):
        super().move()  # 调用父类的移动方法

        self.bullet_counter += 1
        if self.bullet_counter >= self.bullet_frequency:
            bullet_position = [self.position[0] + 20, self.position[1]]
        # 发射子弹
            self.bullets.append(Bullet(bullet_position, 1))
            self.bullet_counter = 0  #重置计数器

        # 移动并绘制每一颗子弹
        for bullet in self.bullets:
            bullet.move()
            bullet.draw()

benemies = [Benermy() for _ in range(3)]

# 创建敌机列表
enemies = [Enermy() for _ in range(2)]

def draw_menu():
    font = pygame.font.Font(None, 36)  # 创建字体对象
    title = font.render("Plane Game", True, (0, 0, 0))  # 创建标题文本对象
    screen.blit(title, (350, 250))  # 绘制标题

    start_button = pygame.Rect(350, 300, 100, 50)  # 创建开始按钮的矩形
    pygame.draw.rect(screen, (0, 255, 0), start_button)  # 绘制开始按钮
    start_text = font.render("Start", True, (0, 0, 0))  # 创建开始按钮的文本对象
    screen.blit(start_text, (365, 310))  # 绘制开始按钮的文本

    quit_button = pygame.Rect(350, 360, 100, 50)  # 创建退出按钮的矩形
    pygame.draw.rect(screen, (255, 0, 0), quit_button)  # 绘制退出按钮
    quit_text = font.render("Quit", True, (0, 0, 0))  # 创建退出按钮的文本对象
    screen.blit(quit_text, (375, 370))  # 绘制退出按钮的文本

    return start_button, quit_button  # 返回按钮的矩形，以便后面检测点击事件

def draw_game_over():
    font = pygame.font.Font(None, 36)  # 创建字体对象
    text = font.render("Game Over", True, (255, 0, 0))  # 创建文本对象
    screen.blit(text, (350, 250))  # 绘制文本

    menu_button = pygame.Rect(350, 300, 100, 50)  # 创建返回主菜单按钮的矩形
    pygame.draw.rect(screen, (0, 0, 255), menu_button)  # 绘制返回主菜单按钮
    menu_text = font.render("Menu", True, (0, 0, 0))  # 创建返回主菜单按钮的文本对象
    screen.blit(menu_text, (365, 310))  # 绘制返回主菜单按钮的文本

    return menu_button  # 返回按钮的矩形，以便后面检测点击事件

while not game_over:
        # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 检查鼠标点击事件
            x, y = pygame.mouse.get_pos()  # 获取鼠标位置
            if game_state == "menu":
                start_button, quit_button = draw_menu()
                if start_button.collidepoint(x, y):  # 如果点击了开始按钮
                    game_state = "playing"  # 切换到游戏状态
                    # 重置飞机的位置
                    plane_position = [200, 500]

                    # 重置每个敌机的位置
                    for enemy in enemies:
                        enemy.reset()

                    for benemie in benemies:
                        benemie.reset()
                    
                elif quit_button.collidepoint(x, y):  # 如果点击了退出按钮
                    pygame.quit()
                    sys.exit()
            elif game_state == "game_over":
                menu_button = draw_game_over()
                if menu_button.collidepoint(x, y):  # 如果点击了返回主菜单按钮
                    game_state = "menu"  # 切换到菜单状态
                    plane_live = 3  # 重置生命值
                    game_over = False  # 重置游戏结束状态

    if game_state == "menu":
        screen.fill((255, 255, 255))  # 清屏
        draw_menu()  # 绘制菜单
    
    elif game_state == "playing":
        # 检查事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # 获取按键信息
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and plane_position[1] > 0:
            plane_position[1] -= 5
        if keys[pygame.K_DOWN] and plane_position[1] < 550:  # 假设窗口高度为600，飞机高度为50
            plane_position[1] += 5
        if keys[pygame.K_LEFT] and plane_position[0] > 0:
            plane_position[0] -= 5
        if keys[pygame.K_RIGHT] and plane_position[0] < 750:  # 假设窗口宽度为800，飞机宽度为50
            plane_position[0] += 5

        # 更新飞机的矩形位置
        plane_rect.topleft = plane_position    

        # 清屏
        screen.fill((255, 255, 255))

        # 绘制飞机
        screen.blit(plane_img, plane_position)

        # 更新无敌时间和飞机的可见性
        if invincible_time > 0:
            invincible_time -= 1
            plane_visible = False # 切换飞机的可见性
        else:
            plane_visible = True  # 如果飞机不再无敌，确保飞机是可见的

        #闪烁
        if plane_visible:
            screen.blit(plane_img,plane_position)
        
        # 移动并绘制每一个敌机
        for enemy in enemies:
            enemy.move()
            enemy.draw()
            enemy_rect = pygame.Rect(enemy.position[0], enemy.position[1], 50, 50)

        for benemie in benemies:
            benemie.move()
            benemie.draw()
            benemy_rect = pygame.Rect(benemie.position[0], benemie.position[1], 50, 50)
        
            for bullet in benemie.bullets:
                bullet_rect = pygame.Rect(bullet.position[0], bullet.position[1], 10, 20)               

                # 检查飞机和敌机是否碰撞
                if (plane_rect.colliderect(benemy_rect) and invincible_time == 0) or (plane_rect.colliderect(bullet_rect) and invincible_time == 0):
                    plane_live -= 1
                    invincible_time = 200
            
            if plane_rect.colliderect(enemy_rect) and invincible_time == 0:
                plane_live -= 1
                invincible_time = 200
        
            if plane_live == 0:
                game_state = "game_over"
                break
        
        #绘制生命值
        font = pygame.font.Font(None, 36)  # 创建字体对象
        text = font.render(f"Lives: {plane_live}", True, (255, 0, 0))  # 创建文本对象
        screen.blit(text, (700, 10))  # 在右上角绘制文本

    elif game_state == "game_over":
        screen.fill((255, 255, 255))  # 清屏
        draw_game_over()  # 绘制结束界面
        
    # 更新屏幕
    pygame.display.flip()