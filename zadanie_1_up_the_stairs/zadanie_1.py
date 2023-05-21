import pygame

pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Вверх по лестнице')

# параметры ступеней
STEP_WIDTH = 20
STEP_HEIGHT = STEP_WIDTH
STEP_COLOR = (255, 255, 255)

# параметры игрока, размеры и цвет шрифта
PLAYER_RADIUS = 10
PLAYER_COLOR = (255, 0, 0)
FONT_SIZE = 20
FONT_COLOR = (255, 255, 255)
clock = pygame.time.Clock()

def game_loop():
    game_exit = False
    # стартовая позиция игрока
    player_x = PLAYER_RADIUS
    player_y = WINDOW_HEIGHT - PLAYER_RADIUS * 3
    # начальные координаты ступеней
    step_x = 0
    step_y = WINDOW_HEIGHT - STEP_HEIGHT
    # создаем счетчик шагов
    step_count = 0

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # удаляем игрока из предыдущей позиции
                    pygame.draw.circle(game_display, (0, 0, 0), (player_x, player_y), PLAYER_RADIUS)
                    # обновляем позицию и счет
                    player_x += 20
                    player_y -= 20
                    step_count += 1

        # рисуем лестницу
        while step_x < WINDOW_WIDTH and step_y >= 0:
            pygame.draw.rect(game_display, STEP_COLOR, [step_x, step_y, STEP_WIDTH, STEP_HEIGHT])
            step_x += STEP_WIDTH
            step_y -= STEP_HEIGHT

        # перемещаем игрока на ступень выше
        pygame.draw.circle(game_display, PLAYER_COLOR, (player_x, player_y), PLAYER_RADIUS)

        # подсчитываем сделанные шаги
        pygame.draw.rect(game_display, (0, 0, 0), (10, 10, 100, FONT_SIZE))
        font = pygame.font.SysFont('Arial', FONT_SIZE)
        text = font.render(f'Шаг: {str(step_count)}', True, FONT_COLOR)
        game_display.blit(text, (10, 10))
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()