grid = []

si = 0
sj = 0

with open('12.txt', 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        grid.append(line[:-1])
        if 'S' in line:
            si = i
            sj = [j for j, c in enumerate(line) if c == 'S'][0]

print(grid, si, sj)

search = [['N' for _ in line] for line in grid]

def BFS(si, sj):
    visited = set([(si, sj)])
    positions = [(si, sj)]


    cycle = 0
    while True:
        next = []
        print('POS:', positions)
        for i, j in positions:
            search[i][j] = str(cycle)
            # print('WTF', i, j)
            # visited.add((i, j))

            val = grid[i][j] if not (i, j) == (si, sj) else 'a'
            if val == 'E':
                print('HIT', i, j, positions)
                return cycle

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = (i + di, j + dj)

                if ni in range(len(grid)) and nj in range(len(grid[0])):
                    if (ni, nj) not in visited:
                        new_val = grid[ni][nj]
                        # print('COMPARE:', new_val, val)
                        if new_val == 'E':
                            if ord(val) >= ord('y'):
                                return cycle + 1
                        elif ord(new_val) - ord(val) <= 1:
                            visited.add((ni, nj))
                            next.append((ni, nj))
                    
        positions = next
        cycle += 1

ans = BFS(si, sj)

print(ans)

for row in search:
    print(' '.join(row))
# print(search)