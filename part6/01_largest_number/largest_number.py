def largest() -> int:
    numbers = []
    with open("numbers.txt") as n:
        for i in n:
            numbers.append(int(i))
    return max(numbers)

if __name__ == "__main__":
    print(largest())