cubes = set()
x_min = 100000
x_max = 0
y_min = 100000
y_max = 0
z_min = 100000
z_max = 0

with open('18.txt', 'r') as file:
    for line in file.readlines():
        line = line[:-1]
        coord = tuple(map(int, line.split(',')))
        cubes.add(coord)
        x, y, z = coord
        if x < x_min:
            x_min = x
        if x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y
        if z < z_min:
            z_min = z
        if z > z_max:
            z_max = z

print(cubes)
print(x_min)

def pocketed(x, y, z):
    for dir in [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]:
        nx = x + dir[0]
        ny = y + dir[1]
        nz = z + dir[2]
        while (nx, ny, nz) not in cubes:
            print(nx, ny, nz, x_min, x_max, y_min, y_max, z_min, z_max)
            if not (nx in range(x_min, x_max + 1) and ny in range(y_min, y_max + 1) and nz in range(z_min, z_max + 1)):
                return False
            nx = nx + dir[0]
            ny = ny + dir[1]
            nz = nz + dir[2]

    return True

print("WHAT")
ans = 0
for x, y, z in cubes:
    print("SEARCH", x, y, z)
    for dir in [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]:
        nx = x + dir[0]
        ny = y + dir[1]
        nz = z + dir[2]
        if (nx, ny, nz) not in cubes and not pocketed(nx, ny, nz):
            print("HIT", nx, ny, nz)
            ans += 1

print(ans)