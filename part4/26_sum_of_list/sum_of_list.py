def list_sum(items1: list, items2: list) -> list:
    result = []
    for x in range(len(items1)):
        result.append(items1[x] + items2[x])
    return result


if __name__ == "__main__":
    print(list_sum([1,2,3], [1,2,3]))