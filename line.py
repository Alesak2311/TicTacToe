class Line:
    def __init__(self, area, start_point, direction):
        self.start_point_y, self.start_point_x = start_point
        self.direction = direction

        self.area = area[self.start_point_y - 4:self.start_point_y + 5, self.start_point_x - 4:self.start_point_x + 5]

        self.line = self.make_line()

    def make_line(self):
        if self.direction == 0:
            return [self.area[4 - i][4] for i in range(5)]
        elif self.direction == 1:
            return [self.area[4 - i][4 + i] for i in range(5)]
        elif self.direction == 2:
            return [self.area[4][4 + i] for i in range(5)]
        elif self.direction == 3:
            return [self.area[4 + i][4 + i] for i in range(5)]
        elif self.direction == 4:
            return [self.area[4 + i][4] for i in range(5)]
        elif self.direction == 5:
            return [self.area[4 + i][4 - i] for i in range(5)]
        elif self.direction == 6:
            return [self.area[4][4 - i] for i in range(5)]
        else:
            return [self.area[4 - i][4 - i] for i in range(5)]

    def __repr__(self):
        return repr(self.line)
