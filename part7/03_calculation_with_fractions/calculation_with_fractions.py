from fractions import Fraction


def fractionate(amount: int) -> list:
    return [Fraction(1, int(amount)) for _ in range(int(amount))]


if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print(fractionate(2))