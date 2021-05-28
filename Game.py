import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.tile_size = 32
        self.size = self.width, self.height = self.tile_size * 20, self.tile_size * 20
        self.background_color = 50, 50, 50
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        while True:
            delta_time = 1 / float(self.clock.tick(60))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            self.update(delta_time, events)
            self.screen.fill(self.background_color)
            self.draw(self.screen)
            pygame.display.flip()

    def update(self, delta_time, events):
        pass

    def draw(self, screen):
        for i in range(20):
            rect = pygame.Rect(self.tile_size * i, self.tile_size * i, self.tile_size, self.tile_size)
            rect2 = pygame.Rect(self.tile_size * i, self.tile_size * (19-i), self.tile_size, self.tile_size)
            
            pygame.draw.rect(screen, (255, 255, 255), rect)
            pygame.draw.rect(screen, (255, 255, 255), rect2)

            play = pygame.image.load("./assets/buttons/play.png")
            pause = pygame.image.load("./assets/buttons/pause.png")
            restart = pygame.image.load("./assets/buttons/reset.png")

            screen.blit(play, (32, 0))
            screen.blit(pause, (64, 0))
            screen.blit(restart, (96, 0))
