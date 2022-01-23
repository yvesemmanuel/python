import turtle

class Losango:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        
    def get_picture(self):
        t = turtle.Turtle()

        bigger_diagonal = max(self.diagonal1, self.diagonal2)
        smaller_diagonal = min(self.diagonal1, self.diagonal2)

        t.forward(bigger_diagonal * 10)
        t.left(180)

        t.forward(smaller_diagonal * 5)
        t.left(90)

        # t.forward(smaller_diagonal * 10)

        turtle.done()
        return "square produced by turtle"


t = Losango(3, 5)

print(t.get_picture())