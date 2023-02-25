def invert(dictionary: dict):
    temp = {}

    for k, i in dictionary.items():
        temp[i] = k
    
    dictionary.clear()

    for k, i in temp.items():
        dictionary[k] = temp[k]


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)