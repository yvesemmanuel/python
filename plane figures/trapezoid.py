import turtle

class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def get_area(self):
        return (self.base1 + self.base2) * self.height / 2

    def get_picture(self):
        t = turtle.Turtle()

        t.forward(self.base1 * 10)
        t.left(120)

        p1 = max(self.base1, self.base2) - min(self.base1, self.base2) / 2
        side = ((p1 ** 2) + (self.height** 2)) ** 0.5
        t.forward(10 * side)
        t.left(60)

        t.forward(self.base2 * 10)
        t.left(60)

        t.forward(10 * side)
        t.left(120)
        
        t.forward((self.base1 + self.base2) * 20)

        turtle.done()
        return "trapezoid produced by turtle"

s = Trapezoid(3, 5, 9)

print(s.get_picture())