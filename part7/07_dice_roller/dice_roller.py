from random import choice


def roll(die: str):
    if die == "A":
        return choice([3, 3, 3, 3, 3, 6])
    if die == "B":
        return choice([2, 2, 2, 5, 5, 5])
    if die == "C":
        return choice([1, 4, 4, 4, 4, 4])


def play(die1: str, die2: str, times: int):
    result = [0, 0, 0]
    while sum(result) < times:
        d1, d2 = roll(die1), roll(die2)
        if d1 == d2:
            result[2] += 1
        elif d1 > d2:
            result[0] += 1
        else:
            result[1] += 1
    return (result[0], result[1], result[2])


if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)