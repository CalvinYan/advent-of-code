funcs = {}
values = {}

def mul(x, y):
    return x * y

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

with open('21.txt', 'r') as file:
    for line in file.readlines():
        line = line[:-1]
        tokens = line.split()

        if len(tokens) == 2:
            id, val = tokens
            values[id[:-1]] = int(val)
        elif len(tokens) == 4:
            id, left, op, right = tokens
            if op == '+':
                op = add
            elif op == '-':
                op = sub
            elif op == '*':
                op = mul
            elif op == '/':
                op = div
            
            funcs[id[:-1]] = [left, right, op]
                
        else:
            print("SOMETHING IS WRONG", line)
            quit()

def eval(id):
    if id in values:
        return values[id]
    left, right, op = funcs[id]

    val = op(eval(left), eval(right))
    values[id] = val
    return val

print(eval('root'))
    

