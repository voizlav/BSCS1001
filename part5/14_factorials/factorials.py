def factorials(n: int):
    result = { 1: 1 }
    for i in range(2, n + 1):
        result[i] = i * result[i - 1]
    return result


if __name__ == "__main__":
    factorials(6)