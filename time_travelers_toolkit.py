import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
import custom_module

current_date_and_time = dt.datetime.now().time()
print(current_date_and_time.strftime('%l:%M%p %Z on %b %d, %Y'))

