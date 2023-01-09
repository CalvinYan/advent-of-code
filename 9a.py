ans = 0

i1 = 0
j1 = 0

i2 = 0
j2 = 0

dir_dict = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

visited = set()

with open('9.txt', 'r') as file:
    for line in file.readlines():

        line = line[:-1]

        dir, num = line.split()

        print(dir, num)

        num = int(num)

        i, j = dir_dict[dir]

        for k in range(num):


            visited.add((i2, j2))

            i1 += i
            j1 += j


            # Orthogonal movement
            if i1 == i2 and abs(j1 - j2) == 2:
                j2 = (j1 + j2) // 2
            
            elif j1 == j2 and abs(i1 - i2) == 2:
                i2 = (i1 + i2) // 2

            # Diagonal movement
            elif abs(i1 - i2) + abs(j1 - j2) > 2:
                if i1 > i2:
                    i2 += 1
                else:
                    i2 -= 1
                
                if j1 > j2:
                    j2 += 1
                else:
                    j2 -= 1

            print(i1, j1, i2, j2)
            
            
print(len(visited))