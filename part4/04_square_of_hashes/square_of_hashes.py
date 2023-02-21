def line(number, string):
    if not string:
        print("*" * number)
    else:
        print(string[0] * number)


def square_of_hashes(size):
    for _ in range(size):
        line(size, "#")


if __name__ == "__main__":
    square_of_hashes(5)
