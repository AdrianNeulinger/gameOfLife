class Logic:
    def __init__(self, xcoor, ycoor):
        self.coordinates = []
        self.xcoor = xcoor
        self.ycoor = ycoor
        for x in range(self.xcoor):
            self.coordinates.append([])
            for y in range(self.ycoor):
                self.coordinates[x].append(0)

    def __str__(self):
        returnstring = ''
        for y in range(self.ycoor):
            row = ''
            for x in range(self.xcoor):
                row += ' {}'.format(self.coordinates[x][y])
            returnstring += row + '\n'
        return returnstring


