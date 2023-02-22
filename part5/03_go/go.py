def who_won(game_board: list) -> int:
    player1, player2 = 0, 0
    
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            player1 += 1 if game_board[i][j] == 1 else 0
            player2 += 1 if game_board[i][j] == 2 else 0
    
    return 1 if player1 > player2 else (2 if player2 > player1 else 0)


if __name__ == "__main__":
    who_won([[1]])