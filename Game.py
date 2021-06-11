import sys
import pygame
from Logic import Logic


class Game:
    def __init__(self):
        pygame.init()
        self.tile_size = 32
        self.size = self.width, self.height = self.tile_size * 20, self.tile_size * 21
        self.background_color = 50, 50, 50
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.logic = Logic(20, 20, self.tile_size)
        self.running = False
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
        self.logic.update(events, self.running)



    def draw(self, screen):
        self.logic.draw(screen)

