from datetime import datetime, timedelta


def main():
    filename = get_filename()
    start_date = get_date()
    days = get_days()
    end_date = start_date + timedelta(days=days - 1)
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    result = f"Time period: {start_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n"
    total_minutes = 0
    day_lines = ""
    for i in range(days):
        print_date = start_date + timedelta(days=i)
        day = get_day(f"{print_date.strftime('%d.%m.%Y')}: ")
        day_lines += f"{print_date.strftime('%d.%m.%Y')}: {day[0]}/{day[1]}/{day[2]}\n"
        total_minutes += sum(day)
    result += f"Total minutes: {total_minutes}\n"
    result += f"Average minutes: {total_minutes / days}\n"
    result += day_lines
    add_to_file(result, filename)


def get_filename():
    return input("Filename: ")


def get_date():
    day, month, year = input("Starting date: ").split(".")
    return datetime(int(year), int(month), int(day))


def get_days():
    return int(input("How many days: "))


def get_day(date: str):
    tv, comp, mob = input(date).split(" ")
    return (int(tv), int(comp), int(mob))


def add_to_file(data: str, filename: str):
    with open(filename, "w") as f:
        f.write(data)


main()