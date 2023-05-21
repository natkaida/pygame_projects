import pygame
import random

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Мерцающие звезды")

# параметры звезд
MAX_STARS = 200
stars = []
for i in range(MAX_STARS):
    star_radius = random.randint(1, 3)
    star_color = (255, 255, 237)
    star_position = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))
    star_expand = True
    star_expand_speed = random.uniform(0.1, 0.5)
    stars.append((star_radius, star_color, star_position, star_expand, star_expand_speed))

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for i in range(MAX_STARS):
        star_radius, star_color, star_position, star_expand, star_expand_speed = stars[i]

        # вычисление радиуса расширения
        if star_expand:
            star_radius += star_expand_speed
            if star_radius >= 5:
                star_expand = False
        else:
            star_radius -= star_expand_speed
            if star_radius <= 1:
                star_expand = True

        # изменяем позиции звезд для создания эффекта мерцания
        star_position = (
            star_position[0] + random.randint(-1, 1),
            star_position[1] + random.randint(-1, 1)
        )

        stars[i] = (star_radius, star_color, star_position, star_expand, star_expand_speed)

    # рисуем звезды
    screen.fill((0, 0, 0))
    for star in stars:
        star_radius, star_color, star_position, _, _ = star
        pygame.draw.circle(screen, star_color, star_position, star_radius)

    pygame.display.update()
    clock.tick(60)
