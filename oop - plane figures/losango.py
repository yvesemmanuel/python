import turtle

class Losango:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def get_area(self):
        return self.diagonal1 * self.diagonal2 / 2