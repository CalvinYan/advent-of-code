cubes = set()
with open('18.txt', 'r') as file:
    for line in file.readlines():
        line = line[:-1]
        cubes.add(tuple(map(int, line.split(','))))

print(cubes)

ans = 0
for x, y, z in cubes:
    for dir in [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]:
        nx = x + dir[0]
        ny = y + dir[1]
        nz = z + dir[2]

        if (nx, ny, nz) not in cubes:
            ans += 1

print(ans)