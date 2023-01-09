X = 1
ans = 0

cycle = 1
queue = []

with open('10.txt') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):

        if cycle in [20, 60, 100, 140, 180, 220]:
            print("CYCLE", cycle, X)
            ans += cycle * X;

        line = line[:-1]
        tokens = line.split(' ')
        if len(tokens) == 1:
            cycle += 1
        
        elif len(tokens) == 2:
            _, num = tokens
            num = int(num)

            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                print("CYCLE", cycle, X, line, i)
                ans += cycle * X; 
            
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

print(ans)

