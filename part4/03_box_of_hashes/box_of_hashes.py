def line(number, string):
    if not string:
        print("*" * number)
    else:
        print(string[0] * number)


def box_of_hashes(height):
    for _ in range(height):
        line(10, "#")


if __name__ == "__main__":
    box_of_hashes(5)
