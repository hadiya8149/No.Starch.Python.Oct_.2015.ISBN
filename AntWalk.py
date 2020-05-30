from random import choice
import matplotlib.pyplot as plt
class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_value = [0]
        self.y_value = [0]
    def FillWalk(self):
        while len(self.x_value)<self.num_points:
            def get_step():
                direction = choice([1,-1])
                distance = choice([0,1,2,3,4])
                step = distance * direction
                return step
            x_step = get_step()
            y_step=get_step()
            next_x = self.x_value[-1]+x_step
            next_y = self.y_value[-1]+y_step
            self.x_value.append(next_x)
            self.y_value.append(next_y)
rw = RandomWalk()
rw.FillWalk()
point_numbers =list(range(rw.num_points))
plt.scatter(rw.x_value, rw.y_value, s=5,c=point_numbers,cmap=plt.cm.Oranges)
plt.show()