def same_chars(string, index1, index2):
    try:
        return string[index1] == string[index2]
    except IndexError:
        return False


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))