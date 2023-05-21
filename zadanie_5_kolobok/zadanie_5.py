import pygame

pygame.init()
background = (24, 113, 147)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 300
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Колобок')

# загружаем изображение Колобка
kolobok = pygame.image.load('kolobok.png')
# стартовый угол вращения и скорость
kolobok_angle = 0
kolobok_rotation_speed = 2

# загружаем фреймы лисы
fox = []
for i in range(8):
    fox.append(pygame.image.load(f'fox{i+1}.png'))

# частота обновления фреймов лисы
fox_frame = 0
fox_frame_rate = 8
fox_frame_timer = 0

# стартовые позиции и скорость движения лисы и Колобка
kolobok_x = 0
kolobok_y = WINDOW_HEIGHT // 2 + kolobok.get_height() // 4 
fox_x = -fox[0].get_width()
fox_y = WINDOW_HEIGHT // 2 - fox[0].get_height() // 2
movement_speed = 3
clock = pygame.time.Clock()

# главный цикл
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    # вращаем изображение Колобка вокруг своей оси
    kolobok_angle += kolobok_rotation_speed
    if kolobok_angle >= 360:
        kolobok_angle = 0
    rotated_kolobok = pygame.transform.rotate(kolobok, kolobok_angle)

    # движение Колобка и лисы слева направо
    kolobok_x += movement_speed
    if kolobok_x > WINDOW_WIDTH:
        kolobok_x = 0 - fox[0].get_width()
    fox_x += movement_speed
    if fox_x > WINDOW_WIDTH:
        fox_x = 0 - fox[0].get_width() 

    # приводим скорость анимации лисы в соответствие с частотой обновления экрана
    fox_frame_timer += clock.tick(60)
    if fox_frame_timer >= 1000 / fox_frame_rate:
        fox_frame_timer -= 1000 / fox_frame_rate
        fox_frame = (fox_frame + 1) % len(fox)

    # рисуем фон, выводим фигуры Колобка и лисы
    game_display.fill(background)
    game_display.blit(rotated_kolobok, (kolobok_x, kolobok_y))
    game_display.blit(fox[fox_frame], (fox_x, fox_y))
    pygame.display.update()

pygame.quit()