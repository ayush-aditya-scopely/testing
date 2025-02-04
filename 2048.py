import random

# Initialize the game board
def initialize_game(size=4):
    board = [[0] * size for _ in range(size)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# Add a new tile (2 or 4) at a random empty position on the board
def add_new_tile(board):
    row, col = random.choice([(r, c) for r in range(len(board)) for c in range(len(board[0])) if board[r][c] == 0])
    board[row][col] = 2 if random.random() < 0.9 else 4

# Print the board nicely
def print_board(board):
    for row in board:
        print(' '.join([str(num).rjust(4) for num in row]))
    print()

# Move and merge tiles in a specific direction
def move(board, direction):
    def compress(row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (len(row) - len(new_row))
        return new_row

    def merge(row):
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_row_left(row):
        return compress(merge(compress(row)))

    if direction == 'left':
        board[:] = [move_row_left(row) for row in board]
    elif direction == 'right':
        board[:] = [move_row_left(row[::-1])[::-1] for row in board]
    elif direction == 'up':
        rotated = [list(row) for row in zip(*board)]
        rotated = [move_row_left(row) for row in rotated]
        board[:] = [list(row) for row in zip(*rotated)]
    elif direction == 'down':
        rotated = [list(row) for row in zip(*board)]
        rotated = [move_row_left(row[::-1])[::-1] for row in rotated]
        board[:] = [list(row) for row in zip(*rotated)]

# Check if any moves are available
def any_moves_available(board):
    for row in board:
        if 0 in row:
            return True
    for r in range(len(board)):
        for c in range(len(board[0]) - 1):
            if board[r][c] == board[r][c + 1] or board[c][r] == board[c + 1][r]:
                return True
    return False

# Main game loop
def main():
    board = initialize_game()
    directions = ['left', 'right', 'up', 'down']
    moves = random.choices(directions, k=10)
    print("Initial board:")
    print_board(board)
    for move_input in moves:
        if any_moves_available(board):
            move(board, move_input)
            add_new_tile(board)
    print("Final board state after 10 random moves:")
    print_board(board)

if __name__ == "__main__":
    main()
