ans = 0
maxes_col = []

grid = []

maxes = set()
with open('8.txt') as file:
    grid = [line[:-1] for line in file.readlines()]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            
            if row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[0]) - 1:
                continue
            item = grid[row][col]


            if row == 44 and col == 32:
                print("WHAT")

            score = 0

            i = 1

            # LEFT:
            while col - i >= 0:
                if grid[row][col - i] >= item:
                    score = i
                    break
                if col - i == 0:
                    print("OK", i)
                    score = i
                    break
                i += 1

            i = 1

            # RIGHT:
            while col + i < len(grid[0]):
                if grid[row][col + i] >= item:
                    score *= i
                    break
                if col + i == len(grid[0]) - 1:
                    score *= i
                    break
                i += 1

            i = 1

            # UP:
            while row - i >= 0:
                if grid[row - i][col] >= item:
                    score *= i
                    break
                if row - i == 0:
                    score *= i
                    break
                i += 1

            i = 1

            # DOWN:
            while row + i < len(grid):
                if grid[row + i][col] >= item:
                    score *= i
                    break
                if row + i == len(grid) - 1:
                    score *= i
                    break
                i += 1
                
            print("R:", row, "C:", col, "S:", score)
                 
            if score > ans:
                if score == 25344: quit()
                ans = score

print(ans)
    