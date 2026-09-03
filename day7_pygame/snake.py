import pygame
import random
import os

pygame.init()
w = 600
h = 400
size = 20
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('贪吃蛇小游戏')

# 直接加载字体文件，避免 SysFont() 在部分 Win11 上枚举注册表时崩溃
def make_font(sz):
    for name in ['simhei.ttf', 'msyh.ttc', 'simsun.ttc', 'Deng.ttf']:
        path = os.path.join('C:/Windows/Fonts', name)
        if os.path.exists(path):
            try:
                return pygame.font.Font(path, sz)
            except Exception:
                continue
    return pygame.font.Font(None, sz)  # 兜底字体（不支持中文，但保证不崩溃）

font = make_font(20)
clock = pygame.time.Clock()

snake = [[8, 6]]
dx = 1
dy = 0


def make_food():
    """生成一个不在蛇身上的食物"""
    while True:
        f = [random.randint(0, w // size - 1), random.randint(0, h // size - 1)]
        if f not in snake:
            return f


food = make_food()
score = 0
running = True

while running:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and dy != 1:
                dx = 0
                dy = -1
            elif e.key == pygame.K_DOWN and dy != -1:
                dx = 0
                dy = 1
            elif e.key == pygame.K_LEFT and dx != 1:
                dx = -1
                dy = 0
            elif e.key == pygame.K_RIGHT and dx != -1:
                dx = 1
                dy = 0

    head = [snake[0][0] + dx, snake[0][1] + dy]

    # 撞墙
    if head[0] < 0 or head[0] >= w // size or head[1] < 0 or head[1] >= h // size:
        print('撞墙了，游戏结束，得分', score)
        running = False
        continue

    if head == food:
        # 吃到食物：尾巴不动、蛇变长，撞到任何一格（包括尾巴）都算死
        if head in snake:
            print('撞到自己了，游戏结束，得分', score)
            running = False
            continue
        snake.insert(0, head)
        score += 1
        if len(snake) >= (w // size) * (h // size):
            print('恭喜通关！蛇占满了整个屏幕，得分', score)
            running = False
            continue
        food = make_food()
    else:
        # 没吃到：尾巴会移开一格，所以允许蛇头进入原尾巴那一格
        if head in snake[:-1]:
            print('撞到自己了，游戏结束，得分', score)
            running = False
            continue
        snake.insert(0, head)
        snake.pop()

    screen.fill((0, 0, 0))
    for s in snake:
        pygame.draw.rect(screen, (0, 200, 0), (s[0] * size, s[1] * size, size - 2, size - 2))
    pygame.draw.rect(screen, (255, 0, 0), (food[0] * size, food[1] * size, size, size))
    text = font.render('得分：' + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()

pygame.quit()
