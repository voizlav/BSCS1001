from string import ascii_lowercase
from random import shuffle


def generate_password(length: int):
    letters = [x for x in ascii_lowercase]
    shuffle(letters)
    return "".join(letters[:length])


if __name__ == "__main__":
    print(generate_password(8))
    print(generate_password(12))
    print(generate_password(3))