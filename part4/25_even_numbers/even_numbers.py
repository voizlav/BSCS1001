def even_numbers(items: list) -> list:
    return [x for x in items if x % 2 == 0]


if __name__ == "__main__":
    print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))