grid = []
with open('23.txt', 'r') as file:
    grid = [line[:-1] for line in file.readlines()]

positions = []

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == '#':
            positions.append((i, j))

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
searches = [[[-1, -1], [-1, 0], [-1, 1]],
            [[1, -1], [1, 0], [1, 1]],
            [[-1, -1], [0, -1], [1, -1]],
            [[-1, 1], [0, 1], [1, 1]]]
area = [[-1, -1], [-1, 0], [-1, 1],
            [1, -1], [1, 0], [1, 1],
            [-1, -1], [0, -1], [1, -1],
            [-1, 1], [0, 1], [1, 1]] 
order = [0, 1, 2, 3]

for round in range(100000):
    # print(positions)
    if round % 10 == 0:
        print("ROUND", round)
    proposals = {}
    new_positions = []
    unmoving = []
    for i, (row, col) in enumerate(positions):
        moving = False
        # Decide whether or not to move
        if not any((row + i, col + j) in positions for i, j in area):
            unmoving.append((row, col))
            continue
        for o in order:
            clear = True
            # Search given direction
            for (si, sj) in searches[o]:
                row_s = row + si
                col_s = col + sj
                if (row_s, col_s) in positions:
                    clear = False

            if clear:
                moving = True
                di, dj = directions[o]
                row_p = row  + di
                col_p = col + dj

                if (row_p, col_p) not in proposals:
                    proposals[(row_p, col_p)] = []
                proposals[(row_p, col_p)].append((row, col))
                break

        
        if not moving:
            unmoving.append((row, col))

    for position, goblins in proposals.items():
        if len(goblins) == 1:
            new_positions.append(position)
        else:
            unmoving.extend(goblins)

    # Update positions
    # if len(unmoving) == len(positions):
        # print(round)
        # quit()
    if len(new_positions) == 0:
        print(round)
        quit()
    positions = unmoving + new_positions
    order = order[1:] + order[:1]

    # print(positions)
    # Print grid
    # min_row = min([p[0] for p in positions])
    # min_col = min([p[1] for p in positions])
    # max_row = max([p[0] for p in positions])
    # max_col = max([p[1] for p in positions])
    # for row in range(min_row, max_):
        # string = ''
        # for 
        # print(str())




print(positions)

min_row = min([p[0] for p in positions])
min_col = min([p[1] for p in positions])
max_row = max([p[0] for p in positions])
max_col = max([p[1] for p in positions])

print(max_row, min_row, max_col, min_col)
print((max_row - min_row + 1) * (max_col - min_col + 1) - len(positions))