# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Join elements of each row with ' | ' and print
        print("-" * 9)          # Print a horizontal line as a separator

# Function to check if a player has won
def check_winner(board, player):
    # Define all possible winning combinations on the board
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Top row
        [board[1][0], board[1][1], board[1][2]],  # Middle row
        [board[2][0], board[2][1], board[2][2]],  # Bottom row
        [board[0][0], board[1][0], board[2][0]],  # Left column
        [board[0][1], board[1][1], board[2][1]],  # Middle column
        [board[0][2], board[1][2], board[2][2]],  # Right column
        [board[0][0], board[1][1], board[2][2]],  # Diagonal from top-left to bottom-right
        [board[0][2], board[1][1], board[2][0]]   # Diagonal from top-right to bottom-left
    ]
    # Check if any of the win conditions are fulfilled by the player
    return [player, player, player] in win_conditions

# Function to check if the board is full
def is_board_full(board):
    # Return True if there are no empty spaces (' ') left on the board
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ']*3 for i in range(3)]  # Initialize the board with empty spaces
    players = ['X', 'O']  # Define the players ('X' goes first, 'O' goes second)
    turn = 0  # Initialize turn counter

    # Continue the game until there's a winner or the board is full
    while not (check_winner(board, 'X') or check_winner(board, 'O')) and not is_board_full(board):
        # Print the current state of the board
        print_board(board)
        # Determine whose turn it is based on the turn counter
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn.")

        # Prompt the current player to input their move
        while True:
            try:
                row, col = map(int, input("Enter row and column numbers (e.g., 0 0): ").split())
                # Check if the chosen position is empty (' ')
                if board[row][col] == ' ':
                    break  # Valid move, exit the loop
                else:
                    print("That position is already taken! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter valid row and column numbers.")

        # Place the current player's marker ('X' or 'O') on the board
        board[row][col] = current_player
        turn += 1  # Increment the turn counter

    # Game ended, print the final state of the board
    print_board(board)

    # Check and print the result of the game
    if check_winner(board, 'X'):
        print("Player X wins!")
    elif check_winner(board, 'O'):
        print("Player O wins!")
    else:
        print("It's a tie!")

# Entry point of the program
if __name__ == "__main__":
    tic_tac_toe()