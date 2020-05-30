"""
how to create a random walk
you have 4 axes she can walk right left backward forward and

"""
from random import choice
import pygal
draw = pygal.XY()


class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_value, self.y_value = [0], [0]

    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            def get_step():
                direction = choice([1, -1])
                distance = choice([0, 1, 2, 3, 4])
                step = direction * distance
                return step

            x_step = get_step()
            y_step = get_step()
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            self.x_value.append(next_x)
            self.y_value.append(next_y)
            draw.add('Ant',[(self.x_value[-1], self.y_value[-1])])


rw = RandomWalk()
rw.fill_walk()
draw.title = 'Ant\'s random walk'
draw.render_to_file('antwalk.svg')
