def longest_series_of_neighbours(items: list) -> int:
    count, result = 0, 0

    for i in range(len(items) - 1):
        next = items[i + 1]
        if items[i] + 1 != next and items[i] - 1 != next:
            count = 0
            continue
        count += 1
        if count > result:
            result = count

    return result + 1


if __name__ == "__main__":
    print(longest_series_of_neighbours([1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]))
