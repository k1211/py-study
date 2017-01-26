# Problem 1
# Fill in the Line class methods to accept coordinate as a pair of tuples and return the slope and distance of the line.

import math


class Line(object):
    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)

    def slope(self):
        return float((self.y1 - self.y2)) / (self.x1 - self.x2)

# Problem 2
# Fill in the class

class Cylinder(object):
        def __init__(self, height=1, radius=1):
            self.height = height
            self.radius = radius

        def volume(self):
            return math.pi * (self.radius ** 2) * self.height

        def surface_area(self):
            return 2 * math.pi * (self.radius ** 2) + 2 * math.pi * self.radius * self.height


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
c = Cylinder(2,3)

print "Distance: " , li.distance()
print "Slope: " , li.slope()
print "Volume: " , c.volume()
print "Surface area: " , c.surface_area()