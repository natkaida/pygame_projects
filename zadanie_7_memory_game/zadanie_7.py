import pygame
from random import shuffle

pygame.init()
# определяем цвета игры
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)
grey = (192, 192, 192)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Тренируем визуальную память")

# задаем параметры окружностей и перемешиваем пары
circle_radius = 50
circle_colors = [red, blue, green, yellow, purple, white]
circle_pairs = circle_colors * 2
shuffle(circle_pairs)

# формируем список окружностей
circle_positions = []
for i in range(6):
    for j in range(2):
        center_x = ((screen_width / 6) * (i + 1)) - (screen_width / 12)
        center_y = ((screen_height / 3) * (j + 1)) - (screen_height / 6)
        circle_positions.append([center_x, center_y])

# запоминаем позиции и цвета окружностей
original_circle_positions = circle_positions.copy()
original_circle_colors = circle_pairs.copy()

# рисуем цветные окружности
for i in range(len(circle_pairs)):
    position = circle_positions[i]
    color = circle_pairs[i]
    pygame.draw.circle(screen, color, position, circle_radius)

font = pygame.font.SysFont('Arial', 20)
pygame.display.update()

# ждем 5 секунд
pygame.time.wait(5000)

# закрываем цветные окружности серыми
for i in range(len(circle_pairs)):
    position = circle_positions[i]
    pygame.draw.circle(screen, grey, position, circle_radius)

pygame.display.update()
uncovered_circles = []
last_uncovered_circle = None
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i in range(len(circle_positions)):
                position = circle_positions[i]
                if ((position[0] - mouse_pos[0]) ** 2 + (position[1] - mouse_pos[1]) ** 2) ** 0.5 < circle_radius:
                    if i not in uncovered_circles:
                        uncovered_circles.append(i)
                        color = original_circle_colors[i]
                        pygame.draw.circle(screen, color, position, circle_radius)
                        pygame.display.update()
                        if last_uncovered_circle is not None and original_circle_colors[last_uncovered_circle] == original_circle_colors[i]:
                            score += 1
                        last_uncovered_circle = i

            if len(uncovered_circles) == len(circle_pairs):
                # вывод результата
                final_score_text = font.render(f"Уровень памяти: {str(score)} из 6", True, white)
                screen.blit(final_score_text, (screen_width // 2, screen_height // 2 + 125))
                pygame.display.update()
                pygame.time.wait(3000)
                pygame.quit()
                exit()
