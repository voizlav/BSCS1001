from string import ascii_lowercase, digits
from random import shuffle, choice


def generate_strong_password(length: int, numbers: bool, symbols: bool):
    result = [choice(ascii_lowercase)]
    pool = ascii_lowercase
    if numbers:
        result += choice(digits)
        pool += digits
    if symbols:
        result += choice("!?=+-()#")
        pool += "!?=+-()#"
    while len(result) != length:
        result += choice(pool)
        shuffle(result)
    return "".join(result)


if __name__ == "__main__":
    print(generate_strong_password(3, True, True))
    print(generate_strong_password(15, True, False))
    print(generate_strong_password(19, False, True))