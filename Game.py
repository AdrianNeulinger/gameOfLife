import sys
import pygame
from Logic import Logic


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game of Life")
        self.tile_size = 32
        self.size = self.width, self.height = self.tile_size * 21, self.tile_size * 23
        self.background_color = 50, 50, 50
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.logic = Logic(21, 21, self.tile_size)
        self.running = False

        self.font = pygame.font.Font('assets/fonts/joystix monospace.ttf', 30)

        self.start_button, self.start_text, self.start_text_rect = self.create_button(
            "START",
            (0, 255, 0),
            0,
            self.tile_size
        )
        self.stop_button, self.stop_text, self.stop_text_rect = self.create_button(
            "STOP",
            (255, 0, 0),
            7,
            self.tile_size
        )
        self.reset_button, self.reset_text, self.reset_text_rect = self.create_button(
            "RESET",
            (255, 255, 255),
            14,
            self.tile_size
        )

        while True:
            delta_time = 1 / float(self.clock.tick(5))
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
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if self.start_button.collidepoint(pos):
                    self.running = True
                if self.stop_button.collidepoint(pos):
                    self.running = False
                if self.reset_button.collidepoint(pos):
                    self.logic = Logic(21, 21, self.tile_size)
                    self.running = False

        self.logic.update(events, self.running)


    def draw(self, screen):
        self.logic.draw(screen)

        pygame.draw.rect(screen, (150, 150, 150), self.start_button)
        screen.blit(self.start_text, self.start_text_rect)
        pygame.draw.rect(screen, (150, 150, 150), self.stop_button)
        screen.blit(self.stop_text, self.stop_text_rect)
        pygame.draw.rect(screen, (150, 150, 150), self.reset_button)
        screen.blit(self.reset_text, self.reset_text_rect)

    def create_button(self, text, color, x, tile_size):
        button = pygame.Rect(
            x * tile_size + 1,
            21 * self.tile_size + 1,
            self.tile_size * 7 - 2,
            self.tile_size * 2 - 2,
        )
        text = self.font.render(text, False, color)
        text_rect = text.get_rect(
            center=(
                x * tile_size + 1 + (self.tile_size * 7 - 2) / 2,
                21 * self.tile_size + (self.tile_size * 2 - 2) / 2
            )
        )
        return [button, text, text_rect]