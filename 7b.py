sizes = {}
children = {}

total_size = 0
with open('7.txt') as file:
    lines = file.readlines()
    dir_stack = []
    for line in lines:
        current = '/'.join(dir_stack)
        # current = dir_stack[-1] if len(dir_stack) > 0 else None
        line = line[:-1]
        tokens = line.split()
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                if tokens[2] == '..':
                    dir_stack = dir_stack[:-1]
                elif tokens[2] == '/':
                    dir_stack = ['/']
                else:
                    dir_stack.append(tokens[2])
            elif tokens[1] == 'ls':
                if current not in sizes:
                    sizes[current] = 0
                if current not in children:
                    children[current] = []
        elif tokens[0].isnumeric():
            sizes[current] += int(tokens[0])
            total_size += int(tokens[0])
        elif tokens[0] == 'dir':
            children[current].append(current + '/' + tokens[1])

# DFS
floor = total_size - 40000000
ans = 1000000000

def DFS(current):
    global ans
    size = sizes[current]

    for child in children[current]:
        size += DFS(child)
    
    if size >= floor:
        print(current, size)
        if size < ans:
            ans = size

    return size

size = DFS('/')

print(ans)