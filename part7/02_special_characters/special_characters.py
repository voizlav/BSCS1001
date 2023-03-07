from string import ascii_letters, punctuation


def separate_characters(my_string: str):
    a, b, c = "", "", ""
    for char in my_string:
        if char in ascii_letters:
            a += char
            continue
        if char in punctuation:
            b += char
            continue
        c += char
    return (a, b, c)


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])