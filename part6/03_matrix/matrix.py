def get_data(file: str) -> list:
    data = []
    with open(file) as f:
        for i in f:
            data.append(i.replace("\n", "").split(","))
    return data


def matrix_sum():
    total = 0
    data = get_data("matrix.txt")
    for row in data:
        total += sum(int(i) for i in row)
    return total


def matrix_max():
    greatest = -float("inf")
    data = get_data("matrix.txt")
    for row in data:
        get_max = max(int(i) for i in row)
        if greatest < get_max:
            greatest = get_max
    return greatest


def row_sums():
    result = []
    data = get_data("matrix.txt")
    for row in data:
        result.append(sum(int(i) for i in row))
    return result


if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
