import time
import random
import json
from itertools import count


class Country:
    def __init__(self, code):
        self.code = code
        self.points = 0
        self.stage_points = 0

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
        country.stage_points = random.random()
        # print(country.code, country.points)

    stage_standings = sorted(countries, key=lambda current_country: current_country.stage_points, reverse=True)
    stage_standings[0].points += 25
    stage_standings[1].points += 18
    stage_standings[2].points += 15
    stage_standings[3].points += 12
    stage_standings[4].points += 10
    stage_standings[5].points += 8
    stage_standings[6].points += 6
    stage_standings[7].points += 4
    stage_standings[8].points += 2
    stage_standings[9].points += 1

    standings = sorted(countries, key=lambda current_country: current_country.points, reverse=True)
    current_place = 1
    best_score = standings[0].points

    for country in standings:
        displayed_score = country.points
        print(current_place, country.code, displayed_score)
        current_place += 1
        if current_place > places_displayed:
            break

    time.sleep(int(time_between_steps))


