import pygame
import random

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Лабиринт')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

# параметры стен и дверей
line_width = 10
line_gap = 40
line_offset = 20
door_width = 20
door_gap = 40
max_openings_per_line = 5

# параметры и стартовая позиция игрока
player_radius = 10
player_speed = 5
player_x = screen_width - 12
player_y = screen_height - line_offset

# рисуем стены и двери
lines = []
for i in range(0, screen_width, line_gap):
    rect = pygame.Rect(i, 0, line_width, screen_height)
    num_openings = random.randint(1, max_openings_per_line)
    if num_openings == 1:
        # одна дверь посередине стены
        door_pos = random.randint(line_offset + door_width, screen_height - line_offset - door_width)
        lines.append(pygame.Rect(i, 0, line_width, door_pos - door_width))
        lines.append(pygame.Rect(i, door_pos + door_width, line_width, screen_height - door_pos - door_width))
    else:
        # несколько дверей
        opening_positions = [0] + sorted([random.randint(line_offset + door_width, screen_height - line_offset - door_width) for _ in range(num_openings-1)]) + [screen_height]
        for j in range(num_openings):
            lines.append(pygame.Rect(i, opening_positions[j], line_width, opening_positions[j+1]-opening_positions[j]-door_width))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # передвижение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > player_radius:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < screen_width - player_radius:
        player_x += player_speed
    elif keys[pygame.K_UP] and player_y > player_radius:
        player_y -= player_speed
    elif keys[pygame.K_DOWN] and player_y < screen_height - player_radius:
        player_y += player_speed

    # проверка столкновений игрока со стенами
    player_rect = pygame.Rect(player_x - player_radius, player_y - player_radius, player_radius * 2, player_radius * 2)
    for line in lines:
        if line.colliderect(player_rect):
            # в случае столкновения возвращаем игрока назад
            if player_x > line.left and player_x < line.right:
                if player_y < line.top:
                    player_y = line.top - player_radius
                else:
                    player_y = line.bottom + player_radius
            elif player_y > line.top and player_y < line.bottom:
                if player_x < line.left:
                    player_x = line.left - player_radius
                else:
                    player_x = line.right + player_radius
    screen.fill(black)
    for line in lines:
        pygame.draw.rect(screen, green, line)
    pygame.draw.circle(screen, red, (player_x, player_y), player_radius)
    pygame.display.update()
    clock.tick(60)