class Line:
    VECTORS = ((-1, 0),
               (-1, 1),
               (0, 1),
               (1, 1),
               (1, 0),
               (1, -1),
               (0, -1),
               (-1, -1))

    def __init__(self, area, start_point, direction):
        self.start_point_y, self.start_point_x = start_point
        self.direction = direction
        self.vector = Line.VECTORS[direction]

        self.area = area

        self.tiles = self.make_line()

    def check_bounds(self):
        if self.vector[0] == 1:
            if len(self.area[self.start_point_y:]) < 5:
                return True
        elif self.vector[0] == -1:
            if len(self.area[:self.start_point_y]) < 4:
                return True

        if self.vector[1] == 1:
            if len(self.area[0][self.start_point_x:]) < 5:
                return True
        elif self.vector[1] == -1:
            if len(self.area[0][:self.start_point_x]) < 4:
                return True

        return False

    def make_line(self):
        if self.check_bounds():
            return []
        else:
            return [self.area[self.start_point_y + self.vector[0] * i]
                    [self.start_point_x + self.vector[1] * i] for i in range(5)]

    def __repr__(self):
        return repr(self.tiles)


class OLine(Line):
    def __init__(self, area, start_point, direction):
        super().__init__(area, start_point, direction)

        self.value = self.evaluate()

    def evaluate(self):
        if 2 in self.tiles:
            return 0

        return self.tiles.count(1)


class XLine(Line):
    def __init__(self, area, start_point, direction):
        super().__init__(area, start_point, direction)

        self.value = self.evaluate()

    def evaluate(self):
        if 1 in self.tiles:
            return 0

        return self.tiles.count(2)
