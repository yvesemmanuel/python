import turtle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return math.pi * math.sqrt(self.radius)
    
    def get_diameter(self):
        return 2 * self.radius
    
    def get_perimeter(self):
        return math.pi * self.get_diameter()
    
    def get_picture(self):
        turtle.Turtle().circle(self.radius * 10)
        turtle.done()
        return "circle produced by turtle"