import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
import custom_module

current_year = dt.date.today().year
current_date_and_time = dt.datetime.now().time()
print(current_date_and_time.strftime('%l:%M%p %Z on %b %d, %Y'))

base_cost = Decimal('8.73')

cost_multiplier = abs(current_year-random_year)

final_cost = base_cost * cost_multiplier
