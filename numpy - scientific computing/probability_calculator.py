from random import choices, shuffle
from copy import copy


class Urn:
    def __init__(self, **kwargs):
        self.contents = list()
        for color in kwargs:
            self.contents.extend([color] * kwargs[color])
        
        shuffle(self.contents)

    def draw(self, n):
        if (n >= len(self.contents)):
            balls_selected = self.contents
        else:
            balls_selected = choices(self.contents, k=n)

        return balls_selected


def experiment(urn, expected_balls, num_balls_drawn, num_experiments):
    experiment_success = 0
    for i in range(num_experiments):
        drawn_balls = urn.draw(num_balls_drawn)

        drawn_success = 0
        for j, k in expected_balls.items():
            if (j in drawn_balls) and (k == drawn_balls.count(j)):
                drawn_success += 1

        if drawn_success == len(expected_balls):
            experiment_success += 1

    return experiment_success / num_experiments


urn = Urn(black=6, red=4, green=3)
probability = experiment(urn=urn,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(probability)