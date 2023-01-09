X = 1
ans = 0

cycle = 1
queue = []

screen = ''

with open('10.txt') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        col = (cycle-1) % 40
        # if col == 0: col = 40

        print("CHECK:", X, col)
        if abs(X - col) <= 1:
            screen += '#'
        else:
            screen += '.'
        # if cycle in [20, 60, 100, 140, 180, 220]:
            # ans += cycle * X;

        line = line[:-1]
        tokens = line.split(' ')
        if len(tokens) == 1:
            cycle += 1
        
        elif len(tokens) == 2:
            _, num = tokens
            num = int(num)

            cycle += 1
            col = (cycle-1) % 40
            # if col == 0: col = 40
            print("CHECK:", X, col)
            if abs(X - col) <= 1:
                screen += '#'
            else:
                screen += '.'
            # if cycle in [20, 60, 100, 140, 180, 220]:
                # ans += cycle * X; 
            
            cycle += 1
            X += num


# while len(queue) > 0:
    # if cycle in [20, 60, 100, 140, 180, 220]:
        # ans += cycle * X; 
    # cycle += 1
# 
    # X += queue[0]
    # queue = queue[1:]
# 
    # print(X, queue)

# print(ans)

for i in range(6):
    print(screen[i * 40:(i + 1) * 40])
