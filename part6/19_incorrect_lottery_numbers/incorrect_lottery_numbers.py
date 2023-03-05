def filter_incorrect():
    load_data = []
    with open("lottery_numbers.csv") as x:
        for i in x:
            line = i.strip().split(";")
            load_data.append(line)

    correct = ""
    for week in load_data:
        x, y = week[0].split(" ")
        try:
            header = f"{x} {int(y)};"
            numbers = [int(num) for num in week[1].split(',') if int(num) > 0 and int(num) < 40]
        except ValueError:
            continue
        unique_numbers = []
        for num in numbers:
            unique_numbers.append(num) if num not in unique_numbers else None
        if not len(unique_numbers) == 7:
            continue
        correct += header
        correct += ",".join(str(num) for num in unique_numbers)
        correct += "\n"
    
    with open("correct_numbers.csv", "w") as c:
        c.write(correct)


if __name__ == "__main__":
    filter_incorrect()