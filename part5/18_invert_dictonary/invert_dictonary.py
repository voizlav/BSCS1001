def invert(dictionary: dict):
    temp = {i: k for k, i in dictionary.items()}
    dictionary.clear()
    for key in temp:
        dictionary[key] = temp[key]


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)