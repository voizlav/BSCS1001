def line(number, string):
    if not string:
        print("*" * number)
    else:
        print(string[0] * number)


def triangle(size, symbol):
    for i in range(size):
        line(i + 1, symbol)


def box(height, width, symbol):
    for _ in range(height):
        line(width, symbol)


def shape(size1, symbol1, size2, symbol2):
    triangle(size1, symbol1)
    box(size2, size1, symbol2)


if __name__ == "__main__":
    shape(5, "x", 2, "o")