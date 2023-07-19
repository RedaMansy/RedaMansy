import datetime
from datetime import date
import enum
import re

def delta_days():

    date_started = datetime.date(2018, 7, 9)
    today = date.today()

    delta = today - date_started

    return delta.days

days = delta_days()

def edit_readme(days):
    with open("README.md") as readmefile:
        data = readmefile.readlines()

    # print(data[11])
    data[11] = f"⚡ Fun fact **I've been journaling every day for {days} days straight**\n"

    with open("README.md", "w") as readmefile:
        readmefile.writelines(data)

edit_readme(days)




