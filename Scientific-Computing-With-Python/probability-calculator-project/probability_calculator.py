import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, count):
        if count >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        drawn = random.sample(self.contents, count)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        drawn_counter = Counter(drawn)
        if all(drawn_counter.get(color, 0) >= count for color, count in expected_balls.items()):
            success += 1
    return success / num_experiments

# Uso de ejemplo
hat = Hat(red=5, blue=3, green=2)
prob1 = experiment(hat, {"red":2, "blue":1}, 4, 1000)
prob2 = experiment(hat, {"red":2, "blue":1}, 4, 1000)

print(prob1)  # Probabilidad 1
print(prob2)  # Probabilidad 2 (debería ser diferente de prob1)
