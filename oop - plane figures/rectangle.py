import turtle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self): return self.width * self.height

    def get_perimeter(self): return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        t = turtle.Turtle()

        t.forward(self.width * 10)
        t.left(90)

        t.forward(self.height * 10)
        t.left(90)

        t.forward(self.width * 10)
        t.left(90)

        t.forward(self.height * 10)
        t.left(90)

        turtle.done()
        return "rectangle produced by turtle"

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_side(self, new_side_length):
        self.width = new_side_length
        self.height = new_side_length

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
    
    def set_height(self, new_height):
        self.width = new_height
        self.height = new_height

    def get_picture(self):
        t = turtle.Turtle()

        t.forward(self.width * 10)
        t.left(90)

        t.forward(self.height * 10)
        t.left(90)

        t.forward(self.width * 10)
        t.left(90)

        t.forward(self.height * 10)
        t.left(90)

        turtle.done()
        return "square produced by turtle"

    def __str__(self):
        return f"Square(side={self.width})"