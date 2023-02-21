def line(number, string):
    if not string:
        print("*" * number)
    else:
        print(string[0] * number)


def triangle(size):
    for i in range(size):
        line(i + 1, "#")


if __name__ == "__main__":
    triangle(5)
