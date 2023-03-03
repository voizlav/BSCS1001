import math


def load_data(filename: str) -> dict:
    data = {}
    with open(filename) as f:
        next(f)
        for i in f:
            line = i.strip().split(";")
            data[line[3]] = {
                "xy": (float(line[0]), float(line[1])),
                "fid": int(line[2]),
                "slot": int(line[4]),
                "operative": True if line[5] == "Yes" else False,
                "id": line[6]
            }
    return data


def get_station_data(filename: str) -> dict:
    result = {}
    data = load_data(filename)
    for station in data:
        result[station] = data[station]["xy"]
    return result


def distance(stations: dict, station1: str, station2: str) -> float:
    x1, y1 = stations[station1]
    x2, y2 = stations[station2]
    x = (x1 - x2) * 55.26
    y = (y1 - y2) * 111.2
    return math.sqrt(x**2 + y**2)


def greatest_distance(stations: dict) -> tuple:
    distances = {}
    greatest = (None, None, 0)
    for stat1 in stations:
        for stat2 in stations:
            distances[(stat1, stat2)] = distance(stations, stat1, stat2)
    for dist in distances:
        if distances[dist] > greatest[2]:
            s1, s2 = dist
            greatest = (s1, s2, distances[dist])
    return greatest


if __name__ == "__main__":
    stations = get_station_data("stations2.csv")
    d = distance(stations, "Karhulantie", "Puistokaari")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    g = greatest_distance(stations)
    print(g)
