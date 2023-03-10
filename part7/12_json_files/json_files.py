from json import loads


def print_persons(filename: str):
    data = loads(load_data(filename))
    for person in data:
       print(f"{person['name']} {person['age']} years ({', '.join(person['hobbies'])})")


def load_data(filename: str):
    with open(filename) as f:
        return f.read()


if __name__ == "__main__":
    print_persons("file1.json")
    print_persons("file2.json")
    print_persons("file3.json")
    print_persons("file4.json")