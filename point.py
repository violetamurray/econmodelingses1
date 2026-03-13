class point:
    """
    Simple class to represent a point in 2D space
    """
    def __init__(self, x, y):
        """
        Constructor for point class.
        :param x: x coordinate of point.
        param y: y coordinate of point.
        """
        self.x = x
        self.y = y
    def __str__(self):
        """
        String representation of point class.
        :return: String representation of point class.
        """
        return f"p<{self.x}, {self.y}>"

p1 = point(1,2)
p2 = point(3,4)


print(p1.x, p1.y)
print(p2.x, p2.y)
print(p1, p2)





