def sum_of_positives(items: list) -> int:
    result = 0
    for i in items:
        if i > 0:
            result += i
    return result


if __name__ == "__main__":
    print(sum_of_positives([2, 2, -3]))