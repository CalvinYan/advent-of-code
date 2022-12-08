with open('5.txt') as file:
    lines = file.readlines()

    stacks = [[] for _ in range(9)]
    for line in lines[:8]:
        for i in range(9):
            if line[4 * i + 1] is not ' ':
                stacks[i].append(line[4 * i + 1])
        
    print(stacks)

    for line in lines[10:]:
        line = line[:-1]
        arr = line.split()
        num = int(arr[1])
        fr = int(arr[3]) - 1
        to = int(arr[5]) - 1

        stacks[to] = stacks[fr][:num] + stacks[to]
        stacks[fr] = stacks[fr][num:]
        
        print('move', num, 'from', fr, 'to', to)
        print(stacks)

print(str([stacks[i][0] for i in range(9)]))