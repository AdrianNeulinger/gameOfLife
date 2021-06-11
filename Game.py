import sys
import pygame
from Logic import Logic


class Game:
    def __init__(self):
        pygame.init()
        self.tile_size = 32
        self.size = self.width, self.height = self.tile_size * 21, self.tile_size * 23
        self.background_color = 50, 50, 50
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.logic = Logic(21, 21, self.tile_size)
        self.running = False

        self.font = pygame.font.Font('assets/fonts/joystix monospace.ttf', 30)
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
        start_text = self.font.render("START", False, (0, 255, 0))

        # draw text
        # font = pygame.font.Font(None, 25)
        # text = font.render("You win!", True, BLACK)
        # text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        # screen.blit(text, text_rect)

        screen.blit(start_text, (self.tile_size, 20 * self.tile_size))
        stop_text = self.font.render("STOP", False, (255, 0, 0))
        screen.blit(stop_text, (self.tile_size * 9, 20 * self.tile_size))
        random_text = self.font.render("RANDOM", False, (255, 255, 255))
        screen.blit(random_text, (self.tile_size * 18, 20 * self.tile_size))
        self.logic.draw(screen)

