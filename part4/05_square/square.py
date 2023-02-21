def line(number, string):
    if not string:
        print("*" * number)
    else:
        print(string[0] * number)


def square(size, character):
    for _ in range(size):
        line(size, character)


if __name__ == "__main__":
    square(5, "x")