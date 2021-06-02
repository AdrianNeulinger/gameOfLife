class Logic():
    def __init__(self, xcoor, ycoor):
        coordinates = []
        for x in range(xcoor):
            coordinates[x] = []
            for y in range(ycoor):
                coordinates[x].append(0)
