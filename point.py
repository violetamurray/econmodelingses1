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
    def __repr__(self):
        return self.__str__()
    def distance_origin(self):
        """
        Calculate the distance between point and origin.
        _return: float, distance between point and origin.
        :return:
        """
        return(self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to(self, point):
        """
        Calculate the distance between current point and another point.
        :param point: the other point to calculate teh distance to.
        :return: float, distance between current point and another point.
        """
        return((self.x-point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
    def __lt__(self, other):
        """
        Returns True is self is less than the other point.
        :param other: the other point to compare against
        :return: True or False
        """
        return self.distance_origin() < other.distance_origin()


p1 = point(1,2)
p2 = point(3,4)


print(p1.x, p1.y)
print(p2.x, p2.y)
print(p1, p2)
print(f"{p2} distance to origin is {p2.distance_origin()}")
p3 = point(12,5)
print(p3.x, p3.y)
print(f"{p3} distance to origin is {p3.distance_origin()}")
p1 = point(6,10)
p2 = point(6,15)
print(f"distance between {p1} and {p2} is {p1.distance_to(p2)}")
p4 = point(1,1)
points = [p1, p2, p3, p4, point(15,6)] #list of points
print(points)
points.sort()
print(points)






