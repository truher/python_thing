"""Produces a date string, e.g. 2024.11.20.06.57"""

import datetime

print(datetime.datetime.now().strftime("%Y.%m.%d.%H.%M"))
