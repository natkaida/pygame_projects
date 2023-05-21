import pygame
import random

class RainSimulator:
    def __init__(self):
        pygame.init()
        self.screen_width = 500
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Дождь")
        self.font = pygame.font.SysFont("Consolas", 20)
        self.background_color = (0, 0, 0)
        self.blue = (173, 216, 230)

        # параметры дождевых капель
        self.drops = []
        self.drops_landed = 0
        self.drops_per_pixel = 100
        self.level_height = 0

        self.clock = pygame.time.Clock()

    # добавляем капли дождя
    def add_drop(self):
        self.drops.append([random.randint(0, self.screen_width), 0])

    # рисуем дождь
    def draw_drops(self):
        for drop in self.drops:
            pygame.draw.line(self.screen, self.blue, (drop[0], drop[1]), (drop[0], drop[1] + 5), 2)

    # подсчитываем капли, поднимаем уровень воды
    def update_drops(self):
        for drop in self.drops:
            drop[1] += 5
            if drop[1] >= self.screen_height:
                self.drops.remove(drop)
                self.drops_landed += 1
                if self.drops_landed % self.drops_per_pixel == 0:
                    self.level_height += 1

    # выводим количество капель
    def draw_score(self):
        score_text = self.font.render(f"Капель дождя: {str(self.drops_landed)}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.draw.rect(self.screen, self.blue, (0, self.screen_height-self.level_height, self.screen_width, self.level_height))

    def run_rain(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.add_drop()
            self.update_drops()
            self.screen.fill(self.background_color)
            self.draw_drops()
            self.draw_score()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    app = RainSimulator()
    app.run_rain()
