import turtle

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def set_sides(self, new_side1, new_side2, new_side3):
        self.side1 = new_side1
        self.side2 = new_side2
        self.side3 = new_side3

    def get_area(self):
        p = (self.get_perimeter()) / 2
        return (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def get_picture(self):
        t = turtle.Turtle()
 
        t.forward(100)
        
        t.left(120)
        t.forward(100)
        
        t.left(120)
        t.forward(100)
        
        turtle.done()

        return "generic triagle form"
    
    def __str__(self):
        if (self.side1 == self.side2 == self.side3):
            return f"Equilateral={self.side1}, side2={self.side2}, side3={self.side3})"
        elif (self.side1 == self.side2) or (self.side1 == self.side3) or (self.side2 == self.side3):
            return f"Isosceles={self.side1}, side2={self.side2}, side3={self.side3})"
        else:
            return f"Scalene={self.side1}, side2={self.side2}, side3={self.side3})"

class ScaleneTriangle(Triangle):
    pass
    
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        self.side1 = side
        self.side2 = side
        self.side3 = side
    
    def get_area(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def get_perimeter(self):
        return 3 * self.side
    
    def get_height(self):
        return self.side * (3 ** 0.5) / 2
    

class IsoscelesTriangle(Triangle):
    def get_height(self):
        if (self.side1 == self.side2):
            L = self.side1
            b = self.side3
        else:
            L = self.side3
            if L != self.side2:
                b = self.side2
            else:
                b = self.side1        

        return ((L ** 2) - ((b ** 2) / 4)) ** 0.5