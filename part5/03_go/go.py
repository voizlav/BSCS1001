def who_won(game_board: list):
    p1, p2 = 0, 0

    for row in game_board:
        for box in row:
            p1 += 1 if box == 1 else 0
            p2 += 1 if box == 2 else 0
    
    return 1 if p1 > p2 else (2 if p2 > p1 else 0)


if __name__ == "__main__":
    who_won([[1]])