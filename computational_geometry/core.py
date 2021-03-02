class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angle(self, other):
        dx = self.x - other.x
        dy = self.x - other.y
        return atan2(dy, dx)

    def distance(self, other):
        """Return the Euclidian distance between two points."""
        dx = self.x - other.x
        dy = self.x - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def determinant(self, other1, other2):
        """Return the determinant of the triangle defined by three points.
        If the determinant is:
            Positive: Counter-clockwise turn
            Negative: Clock-wise turn
            zero: All three points are on a straight line
        """
        x0, y0 = self.x, self.y
        x1, y1 = other1.x, other1.y
        x2, y2 = other2.x, other2.y

        # Compute determinant
        return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)