import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
import custom_module

current_year = dt.date.today().year
current_date_and_time = dt.datetime.now().time()
random_year = randint(int(current_year), 10000)

base_cost = Decimal('8.73')

#incase years are the same add or 1
cost_multiplier = abs(current_year-random_year) or 1

#add round to make sure 2 decimal places
final_cost = round(base_cost * cost_multiplier)

places= ["Glasgow", "Edinburgh", "Manchester", "Chicago", "Cardiff"]

random_place = choice(places)

custom_module.generate_time_travel_message(random_year, random_place, final_cost)



