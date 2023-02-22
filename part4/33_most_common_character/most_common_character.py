def most_common_character(string: str) -> str:
    return max(string, key=string.count)


if __name__ == "__main__":
    print(most_common_character("exemplaryelementary"))