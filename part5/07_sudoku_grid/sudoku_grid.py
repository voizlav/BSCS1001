def row_correct(sudoku: list, row_no: int) -> bool:
    numbers = [i for i in range(1, 10)]
    
    for i in sudoku[row_no]:
        if i not in numbers and i != 0:
            return False
        elif i != 0:
            numbers.remove(i)
    return True


def column_correct(sudoku: list, column_no: int) -> bool:
    numbers = []

    for i in sudoku:
        if i[column_no] > 0 and i[column_no] in numbers:
            return False
        numbers.append(i[column_no])
    return True


def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    numbers = []

    for row in sudoku[row_no:row_no + 3]:
        for box in row[column_no:column_no + 3]:
            if box > 0 and box in numbers:
                return False
            numbers.append(box)
    return True


def sudoku_grid_correct(sudoku: list):

    for row in range(len(sudoku)):
        if not row_correct(sudoku, row):
            return False
    
    for column in range(len(sudoku[0])):
        if not column_correct(sudoku, column):
            return False
    
    for row in range(0, len(sudoku), 3):
        for column in range(0, len(sudoku[row]), 3):
            if not block_correct(sudoku, row, column):
                return False
    
    return True


if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))