
grid = []
path = None


with open('22.txt', 'r') as file:
    lines = [line[:-1] for line in file.readlines()]

    grid = lines[:-2]
    path = lines[-1]
    

# Process path
new_path = []
buffer = ''
for i, c in enumerate(path):
    if c == 'L' or c == 'R':
        new_path.append([int(buffer), c])
        buffer = ''
    else:
        buffer = buffer + c

# Take the last motion into account
new_path.append([int(buffer), 'S'])

path = new_path

# Split grid into faces (this is manually tailored to the input)

faces = {}
# print(grid[:50])
faces['down'] = [line[50:101] for line in grid[:50]]
faces[]
quit()

# Detect boundaries
row_range = []
col_range = []

for row in grid:
    opens = [i for i, c in enumerate(row) if c == '.' or c == '#']
    row_range.append([opens[0], opens[-1]])

for col in range(max([len(row) for row in grid])):
    opens = []
    for i, row in enumerate(grid):
        if col < len(row) and (grid[i][col] == '.' or grid[i][col] == '#'):
            opens.append(i)

    # opens = [i for i, c in enumerate([grid[row][col] for row in range(len(grid))]) if c == '.' and col < len(grid[row])]
    col_range.append([opens[0], opens[-1]])

# print(row_range)
# print(col_range)

facing = 0
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

pos = [0, row_range[0][0]]

for num, turn in path:
    row, col = pos
    dir = dirs[facing]
    for _ in range(num):
        new_row = row + dir[0]
        new_col = col + dir[1]

        # Horizontal movement:
        if dir[0] == 0:
            if new_col < row_range[new_row][0]:
                new_col = row_range[new_row][1]

            elif new_col > row_range[new_row][1]:
                new_col = row_range[new_row][0]

        # Vertical movement
        if dir[1] == 0:
            if new_row < col_range[new_col][0]:
                new_row = col_range[new_col][1]

            elif new_row > col_range[new_col][1]:
                new_row = col_range[new_col][0]

        if grid[new_row][new_col] == '#':
            break
        else:
            row = new_row
            col = new_col

    if turn == 'L':
        facing = (facing + 3) % 4
    elif turn == 'R':
        facing = (facing + 1) % 4

    pos = [row, col]

    print("NEW STATE", pos)

print(pos, facing)
print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + (facing))