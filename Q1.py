import pandas as pd
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# we can used databaase source in this place, used function for date source
def datetime_range(start=None, end=None):
    span = end - start
    for i in range(span.days + 1):
        yield start + timedelta(days=i)

for date in datetime_range(start=datetime(2019, 12, 1), end=datetime(2020, 1, 15)):

    if (date.weekday() == 6):
        dt_wk = date
    else:
       date
    print(date, dt_wk)

