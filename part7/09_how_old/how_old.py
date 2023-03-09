from datetime import datetime, timedelta

get_day = int(input("Day: "))
get_month = int(input("Month: "))
get_year = int(input("Year: "))

set_date = datetime(get_year, get_month, get_day)
millennium  = datetime(1999, 12, 31)
result = set_date - millennium

if result.days < 0:
    print(f"You were {abs(result.days)} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")