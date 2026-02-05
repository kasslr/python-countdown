import datetime
import output
import time
import os

arrival = datetime.datetime(2026,3,10,0,0,0)

def format_timedelta(td):
    total = td.days
    weeks, days = divmod(td.days, 7)
    seconds = td.seconds
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    return f'{weeks} weeks {days} days {hours}h {minutes}m {seconds}s remaining'

while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    today = datetime.datetime.now()
    timeRemaining = arrival - today

    output.generateOutput(format_timedelta(timeRemaining))
    
    time.sleep(1)
