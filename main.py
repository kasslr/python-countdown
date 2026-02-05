import datetime

today = datetime.datetime.now()
arrival = datetime.datetime(2026,3,10)

timeRemaining = arrival - today

def format_timedelta(td):
    total = td.days
    weeks, days = divmod(td.days, 7)

    return f'{weeks} weeks and {days} days remaining'

print(format_timedelta(timeRemaining))