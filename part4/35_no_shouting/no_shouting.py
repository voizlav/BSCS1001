def no_shouting(items: list) -> list:
    return [i for i in items if not i.isupper()]


if __name__ == "__main__":
    print(no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]))