def check_winner(board):# tic toe 1 by ai 
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]
    
    return None

# Example usage with lists
a = ['o', 'x', '-']
b = ['o', 'o', 'x']
c = ['o', 'x', '-']
board = [a, b, c]
winner = check_winner(board)
print(f'Winner: {winner}')

# Function to get board input from the user
def get_board():
    board = []
    for _ in range(3):
        row = input().split()
        board.append(row)
    return board

# Example usage with input
board = get_board()
winner = check_winner(board)
print(f'Winner: {winner}')