#ticktacktoe

def print_board(board):
    """Prints the current state of the game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there is a winner."""
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell != " " for row in board for cell in row)

def main():
    """Main function to run the Tic Tac Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter your row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter your column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already taken! Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()