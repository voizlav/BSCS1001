def spruce(height):
    print("a spruce!")
    whitespace = height - 1
    for i in range(0, height * 2, 2):
        print(f"{' ' * whitespace}{'*' * (i + 1)}")
        whitespace -= 1
    print(f"{' ' * (height - 1)}*")


if __name__ == "__main__":
    spruce(5)