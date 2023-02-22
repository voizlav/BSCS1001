def length_of_longest(items: list) -> int:
    return max(len(i) for i in items)


if __name__ == "__main__":
    print(length_of_longest(["first", "second", "fourth", "eleventh"]))