import random

class Apple:
    apple_counter = 0
    rejected_apples = 0
    total_weight = 0
    apple_weight = 0
    maximum_weight = 300

    def __init__(self):
        self.apple_weight = random.uniform(0.2, 0.5)
        if Apple.total_weight + self.apple_weight <= self.maximum_weight:
            Apple.apple_counter += 1
            Apple.total_weight += self.apple_weight
        else:
            Apple.rejected_apples += 1


number_of_wanted_apples = 1000
apples = []

for x in range(0, number_of_wanted_apples):
    apples.append(Apple())

print('Total number of apples:', Apple.apple_counter)
print('Total number of rejected apples:', Apple.rejected_apples)
print('Total weight:', Apple.total_weight)
