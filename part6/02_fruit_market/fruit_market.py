def read_fruits() -> dict:
    result = {}
    with open("fruits.csv") as f:
        for i in f:
            name, price = i.split(";")
            result[name] = float(price)
    return result


if __name__ == "__main__":
    read_fruits()