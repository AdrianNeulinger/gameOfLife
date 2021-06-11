import pygame


class Logic:
    def __init__(self, xCoor, yCoor, tile_size):
        self.coordinates = []
        self.xCoor = xCoor
        self.yCoor = yCoor
        self.tile_size = tile_size
        for x in range(self.xCoor):
            self.coordinates.append([])
            for y in range(self.yCoor):
                self.coordinates[x].append(0)

    def update(self, events, running):
        if running:
            for x in range(self.xCoor):
                for y in range(self.yCoor):
                    alive_neighbours = self.getNeighbours(x, y)
                    current_state = self.coordinates[x][y]
                    if current_state == 1 and (alive_neighbours < 2 or alive_neighbours > 3):
                        self.coordinates[x][y] = 0
                    elif current_state == 0 and (alive_neighbours == 3):
                        self.coordinates[x][y] = 1

        else:
            try:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        tile_x = int(pos[0] / self.tile_size)
                        tile_y = int(pos[1] / self.tile_size)

                        if self.coordinates[tile_x][tile_y] == 0:
                            self.coordinates[tile_x][tile_y] = 1
                        else:
                            self.coordinates[tile_x][tile_y] = 0
            except IndexError:
                pass

    def getNeighbours(self, xCoor, yCoor):
        aliveNeighbours = 0
        for xOffset in range (-1, 2):
            for yOffset in range(-1, 2):
                if xOffset == 0 and yOffset == 0:
                    continue
                check_x = (xCoor + xOffset) % (len(self.coordinates))
                check_y = (yCoor + yOffset) % len(self.coordinates[0])
                aliveNeighbours += self.coordinates[check_x][check_y]
        return aliveNeighbours

    def draw(self, screen):
        for x in range(self.xCoor):
            for y in range(self.yCoor):
                cell = pygame.Rect(
                    self.tile_size * x + 1,
                    self.tile_size * y + 1,
                    self.tile_size - 2,
                    self.tile_size - 2
                )
                if self.coordinates[x][y] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), cell)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), cell)

    def __str__(self):
        returnstring = ''
        for y in range(self.yCoor):
            row = ''
            for x in range(self.xCoor):
                row += ' {}'.format(self.coordinates[x][y])
            returnstring += row + '\n'
        return returnstring


