def count_matching_elements(my_matrix: list, element: int) -> int:
    counter = 0
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            counter += 1 if my_matrix[i][j] == element else 0
    return counter


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))