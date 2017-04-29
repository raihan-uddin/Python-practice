
class Line(object):
    """
    coordinate as a pair of tuples and return the slope and distance of the line.
    """
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2-y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return float((y2 - y1))/ (x2 - x1)

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())



class Cylinder(object):
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * (3.14)* (self.radius) ** 2

    def surface_are(self):
        top = (3.14) * (self.radius) ** 2
        return 2 * top + 2 * 3.14 * self.radius * self.height


c = Cylinder(2,3)
print(c.volume())
print(c.surface_are())