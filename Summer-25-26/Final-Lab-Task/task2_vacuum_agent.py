# Final Lab Task 2 - Vacuum Cleaning Agent

ROWS = 4
COLS = 4

# D = dirty, . = clean
grid = [
    ['D', '.', 'D', '.'],
    ['D', '.', 'D', '.'],
    ['D', '.', '.', '.'],
    ['D', 'D', 'D', 'D'],
]

row = 0
col = 0
cleaned = 0


def show_environment():
    # A shows where the agent is
    for r in range(ROWS):
        for c in range(COLS):
            if r == row and c == col:
                print('A', end=' ')
            else:
                print(grid[r][c], end=' ')
        print()
    print('-' * 20)


def move(direction):
    # move one cell in the given direction
    global row, col
    if direction == 'right' and col < COLS - 1:
        col = col + 1
    elif direction == 'left' and col > 0:
        col = col - 1
    elif direction == 'down' and row < ROWS - 1:
        row = row + 1
    elif direction == 'up' and row > 0:
        row = row - 1


print("Initial Environment:")
show_environment()

# main loop - clean if dirty, otherwise move
while True:
    if grid[row][col] == 'D':
        grid[row][col] = '.'
        cleaned = cleaned + 1
        print("Cleaned cell at (" + str(row) + ", " + str(col) + ")")
        show_environment()
    elif col < COLS - 1:
        move('right')
        show_environment()
    elif row < ROWS - 1:
        move('down')
        while col > 0:              # back to the first column
            move('left')
        show_environment()
    else:
        show_environment()
        break

print("Cleaning complete. Total cells cleaned:", cleaned)
