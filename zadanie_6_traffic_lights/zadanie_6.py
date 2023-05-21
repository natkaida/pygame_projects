import pygame
import random

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Светофор')
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
DARK_GRAY = (64, 64, 64)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


def game_loop():
    game_exit = False

    # определяем цвета для светофора
    colors = [RED, YELLOW, GREEN]
    active_index = 0
    last_switch = pygame.time.get_ticks()
    interval = 2000

    # параметры автомобилей
    car_width = 40
    car_height = 60
    car_speed = 2
    horizontal_spacing = 12
    vertical_spacing = 20
    car_rects = []
    for i in range(2):
        left_rect = pygame.Rect(100, random.randint(50, WINDOW_HEIGHT - car_height), car_width, car_height)
        right_rect = pygame.Rect(WINDOW_WIDTH - 300 - car_width, random.randint(50, WINDOW_HEIGHT - car_height), car_width, car_height)
        car_rects.append(left_rect)
        car_rects.append(right_rect)

    # вертикальная и горизонтальная дистанция между автомобилями
    for i in range(1, len(car_rects)):
        if car_rects[i].left - car_rects[i-1].right < horizontal_spacing:
            car_rects[i].left = car_rects[i-1].right + horizontal_spacing
        if car_rects[i].top - car_rects[i-1].bottom < vertical_spacing:
            car_rects[i].top = car_rects[i-1].bottom + vertical_spacing

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        # определяем нужный цвет светофора
        now = pygame.time.get_ticks()
        if now - last_switch >= interval:
            active_index = (active_index + 1) % len(colors)
            last_switch = now

        # временной интервал для зеленого цвета - 6 секунд, для остальных - 2
        interval = 6000 if active_index == 2 else 2000

        # движение машин
        if active_index == 0 or active_index == 1:
            car_speed = 0
        else:
            car_speed = 2
        for car_rect in car_rects:
            car_rect.move_ip(0, -car_speed)
            if car_rect.bottom <= 0:
                car_rect.top = WINDOW_HEIGHT
                car_rect.left = 100 if car_rect.left == WINDOW_WIDTH - 100 - car_width else WINDOW_WIDTH - 100 - car_width

        # рисуем светофор
        game_display.fill(GRAY)
        light_rect = pygame.Rect((WINDOW_WIDTH - 200) // 2, (WINDOW_HEIGHT - 300) // 2, 100, 300)
        pygame.draw.rect(game_display, DARK_GRAY, light_rect, 5)
        light_width = light_rect.width
        light_height = light_rect.height // 3
        light_y = light_rect.top
        for i in range(3):
            circle_rect = pygame.Rect(light_rect.left + 10, light_y + i * light_height + 10, light_width - 20, light_height - 20)
            circle_color = colors[i] if i == active_index else BLACK
            pygame.draw.circle(game_display, circle_color, circle_rect.center, circle_rect.width // 2)

        # рисуем автомобили
        for car_rect in car_rects:
            pygame.draw.rect(game_display, BLUE, car_rect)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
game_loop()