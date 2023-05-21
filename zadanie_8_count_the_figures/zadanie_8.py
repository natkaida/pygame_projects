import pygame
import random

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Подсчет фигур")
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# параметры фигур
class Circle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 30

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Triangle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 60
        self.height = 60

    def draw(self):
        pygame.draw.polygon(screen, self.color, [(self.x, self.y), (self.x + self.width, self.y), (self.x + self.width/2, self.y - self.height)])

class Square:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 60
        self.height = 60

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# создаем список фигур
shapes = []
x = random.randint(0, width - 60)
y = random.randint(-500, -50)
color = random.choice(colors)
shape_type = random.choice(["circle", "triangle", "square"])
if shape_type == "circle":
    shape = Circle(x, y, color)
elif shape_type == "triangle":
    shape = Triangle(x, y, color)
else:
    shape = Square(x, y, color)
shapes.append(shape)

# счетчики фигур
circle_count = 0
triangle_count = 0
square_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(black)

    # рисуем и подсчитываем фигуры
    for shape in shapes:
        shape.draw()
        shape.y += 5
        if shape.y > height:
            shapes.remove(shape)
            if isinstance(shape, Circle):
                circle_count += 1
            elif isinstance(shape, Triangle):
                triangle_count += 1
            else:
                square_count += 1
            x = random.randint(0, width - 60)
            y = random.randint(-500, -50)
            color = random.choice(colors)
            shape_type = random.choice(["circle", "triangle", "square"])
            if shape_type == "circle":
                shape = Circle(x, y, color)
            elif shape_type == "triangle":
                shape = Triangle(x, y, color)
            else:
                shape = Square(x, y, color)
            shapes.append(shape)

    # выводим счетчики
    font = pygame.font.SysFont("Verdana", 25)
    circle_text = font.render(f"Окружности: {circle_count}", True, white)
    triangle_text = font.render(f"Треугольники: {triangle_count}", True, white)
    square_text = font.render(f"Квадраты: {square_count}", True, white)
    screen.blit(circle_text, (10, 10))
    screen.blit(triangle_text, (10, 40))
    screen.blit(square_text, (10, 70))

    pygame.display.update()
    clock.tick(60)
