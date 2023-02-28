def print_sudoku(sudoku: list):
    for x in range(len(sudoku)):
        for i in range(len(sudoku[x])):
            print(f"{sudoku[x][i] if not sudoku[x][i] == 0 else '_'} ", end="")
            print(" ", end="") if (i + 1) % 3 == 0 else None 
        print("\n") if (x + 1) % 3 == 0 else print()    


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    result = [x[:] for x in sudoku]
    result[row_no][column_no] = number
    return result


if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 1, 1, 5)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)