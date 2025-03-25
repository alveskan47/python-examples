import time
import random
import json
from itertools import count


class Country:
    def __init__(self, code):
        self.code = code
        self.points = 0

# settings
number_of_steps = 1000
time_between_steps = 2
places_displayed = 10

# Open and read the JSON file
with open('current-countries.json', 'r') as file:
    data = json.load(file)


countries = []
standings = []

for element in data['countries']:
    countries.append(Country(element['code']))

print('\n')
print("Elements:", len(countries))
time.sleep(int(time_between_steps))

for step in range(1, number_of_steps+1):
    print('\n')
    print("Stage:", step, "/", number_of_steps)

    for country in countries:
        country.points += random.random()
        # print(country.code, country.points)

    standings = sorted(countries, key=lambda current_country: current_country.points, reverse=True)
    current_place = 1
    best_score = standings[0].points

    for country in standings:
        displayed_score = "{:.3f}".format(round(best_score - country.points, 3))
        print(current_place, country.code, displayed_score)
        current_place += 1
        if current_place > places_displayed:
            break

    time.sleep(int(time_between_steps))


