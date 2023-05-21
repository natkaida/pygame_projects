import pygame
import random

class RewardsBombs():
    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Призы и бомбы")
        self.clock = pygame.time.Clock()
        self.green_pos = [self.screen_width // 2, self.screen_height - 30]
        self.red_positions = []
        self.red_speed = 2
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 24)
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.green_pos[0] - 20 >= 0:
                            self.green_pos[0] -= 20
                    elif event.key == pygame.K_RIGHT:
                        if self.green_pos[0] + 20 <= self.screen_width:
                            self.green_pos[0] += 20
                    elif event.key == pygame.K_UP:
                        if self.green_pos[1] - 20 >= 0:
                            self.green_pos[1] -= 20
                    elif event.key == pygame.K_DOWN:
                        if self.green_pos[1] + 20 <= self.screen_height:
                            self.green_pos[1] += 20

            # движение красных бомб
            for i in range(len(self.red_positions)):
                self.red_positions[i][1] += self.red_speed

            # создание бомб и призов
            if random.random() < 0.02:
                x = random.randint(0, self.screen_width)
                num = random.randint(1, 10)
                if num % 2 == 0:
                    self.red_positions.append([x, 0, False])
                else:
                    self.red_positions.append([x, 0, True])

            # проверка столкновений с игроком
            for pos in self.red_positions:
                if pos[2]:
                    if abs(pos[0] - self.green_pos[0]) <= 20 and abs(pos[1] - self.green_pos[1]) <= 20:
                        self.score += 1
                        self.red_positions.remove(pos)
                else:
                    if (pos[0] - self.green_pos[0]) ** 2 + (pos[1] - self.green_pos[1]) ** 2 < 400:
                        self.game_over()

            # убираем бомбы за пределами окна
            self.red_positions = [pos for pos in self.red_positions if pos[1] < self.screen_height]
            self.screen.fill((0, 0, 0))

            for pos in self.red_positions:
                if pos[2]:
                    pygame.draw.polygon(self.screen, (0, 0, 255), [[pos[0], pos[1]-10], [pos[0]+10, pos[1]+10], [pos[0]-10, pos[1]+10]])
                else:
                    pygame.draw.circle(self.screen, (255, 0, 0), pos[:2], 10)

            pygame.draw.circle(self.screen, (0, 255, 0), self.green_pos, 10)

            self.draw_score()
            pygame.display.update()
            self.clock.tick(60)

    def draw_score(self):
        score_surface = self.font.render(f"Призы: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))

    def game_over(self):
        message_surface = self.font.render(f"Игра закончена! Призы: {self.score}", True, (255, 0, 0))
        self.screen.blit(message_surface, (self.screen_width // 2 - message_surface.get_width() // 2, self.screen_height // 2 - message_surface.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        exit()

if __name__ == "__main__":
    RewardsBombs()