import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def find_random_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        player_move = input("Enter your move (row column): ").split()
        row, col = map(int, player_move)
        
        if board[row][col] != " ":
            print("Invalid move. That spot is already taken.")
            continue
        
        board[row][col] = "X"
        print_board(board)
        
        if check_winner(board, "X"):
            print("You win! Congratulations!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break
        
        ai_move = find_random_move(board)
        board[ai_move[0]][ai_move[1]] = "O"
        print("AI's move:")
        print_board(board)
        
        if check_winner(board, "O"):
            print("AI wins! Try again.")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
