from copy import deepcopy

import pygame


class Logic:
    def __init__(self, x_coor, y_coor, tile_size):
        # initialize Logic
        self.coordinates = []
        self.updated_map = []
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.tile_size = tile_size
        # fill initial game state with '0'
        for x in range(self.x_coor):
            self.coordinates.append([])
            for y in range(self.y_coor):
                self.coordinates[x].append(0)
        self.updated_map = deepcopy(self.coordinates)

    def update(self, events, running):
        # check if game is running
        if running:
            for x in range(self.x_coor):
                for y in range(self.y_coor):
                    # calculate next state for each cell
                    alive_neighbours = self.get_neighbours(x, y)
                    current_state = self.coordinates[x][y]
                    if current_state == 1 and (alive_neighbours < 2 or alive_neighbours > 3):
                        self.updated_map[x][y] = 0
                    elif current_state == 0 and (alive_neighbours == 3):
                        self.updated_map[x][y] = 1
            # deepcopy needed for updating cells
            self.coordinates = deepcopy(self.updated_map)

        else:
            try:
                # flip cell state on click to set new patterns
                for event in events:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        pos = pygame.mouse.get_pos()
                        tile_x = int(pos[0] / self.tile_size)
                        tile_y = int(pos[1] / self.tile_size)

                        if self.coordinates[tile_x][tile_y] == 0:
                            self.coordinates[tile_x][tile_y] = 1
                        else:
                            self.coordinates[tile_x][tile_y] = 0
            except IndexError:
                pass
            self.updated_map = deepcopy(self.coordinates)

    def get_neighbours(self, x_coor, y_coor):
        alive_neighbours = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                if x_offset == 0 and y_offset == 0:
                    continue
                check_x = (x_coor + x_offset) % (len(self.coordinates))
                check_y = (y_coor + y_offset) % len(self.coordinates[0])
                alive_neighbours += self.coordinates[check_x][check_y]
        return alive_neighbours

    def draw(self, screen):
        # draw rect for each cell, if it's alive
        for x in range(self.x_coor):
            for y in range(self.y_coor):
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
        # string representation of game state
        returnstring = ''
        for y in range(self.y_coor):
            row = ''
            for x in range(self.x_coor):
                row += ' {}'.format(self.coordinates[x][y])
            returnstring += row + '\n'
        return returnstring
