def shortest(items: list) -> str:
    return min(items, key=len)


if __name__ == "__main__":
    print(shortest(["first", "second", "fourth", "eleventh"]))