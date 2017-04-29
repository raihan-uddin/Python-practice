class Circle(object):
    # Class object attribute
    pi = 3.14

    # Circle get instantiated with radius (default is 1
    def __init__(self, radius=1):
        self.radius = radius

    # Area method calculates the area. Note the use of self
    def area(self):
        # radius**2 * pi
        return (self.radius ** 2) * Circle.pi

    # Method for resetting Radius
    def setRadius(self, radius):
        """
        This methods takes in a radius, and resets the curren radius of the Circle
        :param radius:
        :return: radius
        """
        self.radius = radius

    # Method for getting radius (Smae as just calling .radius
    def getRadius(self):
        return self.radius


c = Circle(radius=100)
print(c)
print(c.pi)
print(c.radius)
print(c.area())

c.setRadius(20)
print(c.radius)
print(c.area())
print(c.getRadius())
