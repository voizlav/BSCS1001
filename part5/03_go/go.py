def who_won(game_board: list):
    player1, player2 = 0, 0

    for row in game_board:
        for box in row:
            player1 += 1 if box == 1 else 0
            player2 += 1 if box == 2 else 0
    
    return 1 if player1 > player2 else (2 if player2 > player1 else 0)


if __name__ == "__main__":
    who_won([[1]])