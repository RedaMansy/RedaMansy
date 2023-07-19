import datetime
from datetime import date

def delta_days():
    
    date_started = datetime.date(2018, 7, 9)
    today = date.today()

    delta = today - date_started

    return delta.days
