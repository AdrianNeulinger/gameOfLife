import sys
import pygame
from Logic import Logic


class Game:
    def __init__(self):

        # Create Playing Field and set size

        pygame.init()
        pygame.display.set_caption("Game of Life")
        self.tile_size = 16
        self.size = self.width, self.height = self.tile_size * 42, self.tile_size * 46
        self.background_color = 50, 50, 50
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.logic = Logic(42, 42, self.tile_size)
        self.running = False

        self.font = pygame.font.Font('assets/fonts/joystix monospace.ttf', 30)

        # Create UI Buttons
        self.start_button, self.start_text, self.start_text_rect = self.create_button(
            "START",
            (0, 255, 0),
            0
        )
        self.stop_button, self.stop_text, self.stop_text_rect = self.create_button(
            "STOP",
            (255, 0, 0),
            7
        )
        self.reset_button, self.reset_text, self.reset_text_rect = self.create_button(
            "RESET",
            (255, 255, 255),
            14
        )

        # GAME LOOP

        while True:
            delta_time = 1 / float(self.clock.tick(5))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            # Update entities
            self.update(delta_time, events)
            # Reset Screen
            self.screen.fill(self.background_color)
            # Draw new frame
            self.draw(self.screen)
            pygame.display.flip()

    def update(self, delta_time, events):
        # capture Button clicks
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if self.start_button.collidepoint(pos):
                    self.running = True
                if self.stop_button.collidepoint(pos):
                    self.running = False
                if self.reset_button.collidepoint(pos):
                    self.logic = Logic(42, 42, self.tile_size)
                    self.running = False

        # handle game update logic

        self.logic.update(events, self.running)

    def draw(self, screen):
        # draw game
        self.logic.draw(screen)

        # draw buttons
        pygame.draw.rect(screen, (150, 150, 150), self.start_button)
        screen.blit(self.start_text, self.start_text_rect)
        pygame.draw.rect(screen, (150, 150, 150), self.stop_button)
        screen.blit(self.stop_text, self.stop_text_rect)
        pygame.draw.rect(screen, (150, 150, 150), self.reset_button)
        screen.blit(self.reset_text, self.reset_text_rect)

    def create_button(self, text, color, x):
        # helper function for  creating buttons
        button = pygame.Rect(
            x * 32 + 1,
            21 * 32 + 1,
            32 * 7 - 2,
            32 * 2 - 2,
        )
        text = self.font.render(text, False, color)
        text_rect = text.get_rect(
            center=(
                x * 32 + 1 + (32 * 7 - 2) / 2,
                21 * 32 + (32 * 2 - 2) / 2
            )
        )
        return [button, text, text_rect]
