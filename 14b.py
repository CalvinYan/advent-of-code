import numpy as np

obstructed = set()
max_y = 0
with open('14.txt', 'r') as file:
    lines = [l[:-1] for l in file.readlines()]

    for line in lines:
        coords = line.split()[::2]
        for i, c in enumerate(coords):
            c = c.split(',')
            coords[i] = (int(c[0]), int(c[1]))

        print(coords)
        for (fx, fy), (tx, ty) in zip(coords[:-1], coords[1:]):

            # fx = int(fx)
            # fy = int(fy)
            # tx = int(tx)
            # ty = int(ty)

            while fx != tx or fy != ty:
                obstructed.add((fx, fy))

                if fx < tx:
                    fx += 1
                elif fx > tx:
                    fx -= 1

                if fy < ty:
                    fy += 1
                elif fy > ty:
                    fy -= 1

            obstructed.add((tx, ty))

        # Set boundary line
    max_y = np.max([y for _, y in obstructed])

    # Preprocess
    for x in range(-1000, 1000):
        obstructed.add((x, max_y + 2))

    ans = 0

    while True:
        x = 500
        y = 0

        # Drop sand
        while (500, 0) not in obstructed:
            dir = [(0, 1), (-1, 1), (1, 1)]
            for d in dir:
                nx = x + d[0]
                ny = y + d[1]

                if (nx, ny) not in obstructed:
                    x = nx
                    y = ny
                    break

            if not (x == nx and y == ny):
                obstructed.add((x, y))
                ans += 1
                x = 500
                y = 0
            
        print(ans)
        quit()


