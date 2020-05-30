from random import randint
import pygal


class Die():  # a class representing a single die
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


# Create a D6
# Make some rolls, and store results in a list.
dice = Die()
dice2 = Die()
# store the result of rolling two dice over 100 times
results = [dice.roll() + dice2.roll() for i in range(100)]

max_result = dice.num_sides + dice2.num_sides
# store the frequency of rolled dices
frequencies = [results.count(value) for value in range(1, max_result + 1)]
# visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling two D6 100 times"
hist.x_labels = [str(i) for i in range(1, dice.num_sides + dice2.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6-1', frequencies)
hist.add('D6-2', frequencies)

hist.render_to_file('die_visual.svg')
