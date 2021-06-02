class Logic:
    def __init__(self, xCoor, yCoor):
        self.coordinates = []
        self.xCoor = xCoor
        self.yCoor = yCoor
        for x in range(self.xCoor):
            self.coordinates.append([])
            for y in range(self.yCoor):
                self.coordinates[x].append(0)

    def update(self):
        for x in range(self.xCoor):
            for y in range(self.yCoor):
                pass
                # function to determine future state of a single cell

    def getNeigbours(self, xCoor, yCoor):
        aliveNeigbours = 0
        for xOffset in range (-1, 2):
            for yOffset in range(-1, 2):
                if xOffset == 0 and yOffset == 0:
                    continue
                aliveNeigbours += self.coordinates[xCoor + xOffset][yCoor + yOffset]
        return aliveNeigbours


    def draw(self):
        pass

    def __str__(self):
        returnstring = ''
        for y in range(self.yCoor):
            row = ''
            for x in range(self.xCoor):
                row += ' {}'.format(self.coordinates[x][y])
            returnstring += row + '\n'
        return returnstring


