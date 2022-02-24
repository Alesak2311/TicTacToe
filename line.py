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

        self.area = area[self.start_point_y - 4:self.start_point_y + 5, self.start_point_x - 4:self.start_point_x + 5]

        self.line = self.make_line()

        self.value = self.evaluate()

    def make_line(self):
        return [self.area[4 + self.vector[0] * i][4 + self.vector[1] * i] for i in range(5)]

    def evaluate(self):
        return

    def __repr__(self):
        return repr(self.line)


class OLine(Line):
    def evaluate(self):
        if 2 in self.line:
            return 0

        return self.line.count(1)


class XLine(Line):
    def evaluate(self):
        if 1 in self.line:
            return 0

        return self.line.count(2)
