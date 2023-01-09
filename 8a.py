ans = 0
maxes_col = []

grid = []

maxes = set()
with open('8.txt') as file:
    grid = [line[:-1] for line in file.readlines()]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            
            print("ROW:", row, "COL:", col)
            # Literal edge case
            if row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[0]) - 1:
                ans += 1
                continue

            item = grid[row][col]
            print("ITEM:", item)

            # Left
            if item > max(grid[row][:col]):
                if row == 97 and col == 87:
                    print("LEFT")
                ans += 1
            # Right
            elif item > max(grid[row][col + 1:]):
                if row == 97 and col == 87:
                    print("RIGHT")
                ans += 1
            # Up
            elif item > max([grid[r][col] for r in range(row)]):
                if row == 97 and col == 87:
                    print("UP")
                ans += 1
            # Down
            elif item > max([grid[r][col] for r in range(row + 1, len(grid))]):
                if row == 97 and col == 87:
                    print("DOWN")
                ans += 1
            
            print(ans)

print(ans)
    