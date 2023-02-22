def distinct_numbers(items: list) -> list:
    return sorted(list(set(items)))

if __name__ == "__main__":
    print(distinct_numbers([1, 2, 2, 1, 3]))