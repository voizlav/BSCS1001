def read_input(q: str, x: int, y: int) -> int:
    error = f"You must type in an integer between {x} and {y}"
    while True:
        try:
            num = int(input(q))
            if num >= x and num <= y:
                return num
        except ValueError:
            pass
        print(error)


if __name__ == "__main__":
    read_input("Please type in a number: ", 5, 10)