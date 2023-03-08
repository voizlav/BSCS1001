from random import shuffle


def lottery_numbers(amount: int, lower: int, upper: int):
    pool = [x for x in range(lower, upper + 1)]
    shuffle(pool)
    return sorted(pool[:amount])


if __name__ == "__main__":
    print(lottery_numbers(7, 1, 40))
    print(lottery_numbers(3, 5, 10))