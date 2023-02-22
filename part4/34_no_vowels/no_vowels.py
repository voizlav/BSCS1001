def no_vowels(string: str) -> str:
    return "".join([i for i in string if i not in "aeiou"])


if __name__ == "__main__":
    print(no_vowels("this is an example"))