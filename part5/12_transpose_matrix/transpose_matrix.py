def transpose(matrix: list) -> list:
    result = []
    for i in range(len(matrix)):
        result.append([j[i] for j in matrix])
    
    for x in range(len(result)):
        for z in range(len(result[x])):
            matrix[x][z] = result[x][z]


if __name__ == "__main__":
    test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    test2 = [[1, 1], [2, 2]]
    transpose(test1)
    transpose(test2)
    print(test1)
    print(test2)