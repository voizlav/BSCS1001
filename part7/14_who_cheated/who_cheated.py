from csv import reader


def cheaters():
    start_times, cheater = {}, []
    with open("start_times.csv") as f:
        for line in reader(f, delimiter=";"):
            h, m = line[1].split(":")
            start_times[line[0]] = (int(h) * 60) + int(m)
    with open("submissions.csv") as f:
        for line in reader(f, delimiter=";"):
                h, m = line[3].split(":")
                t = (int(h) * 60) + int(m)
                if t - start_times[line[0]] > 180 and not line[0] in cheater:
                    cheater.append(line[0])
    return cheater


if __name__ == "__main__":
    for cheater in cheaters():
        print(cheater)