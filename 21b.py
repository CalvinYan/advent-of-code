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

# Reverse the functions of values dependent on humn

def determinate(id):
    print("CHECKING ID", id)
    if id == 'humn':
        return 1

    if id == 'root':
        return 0
    
    if id in values:
        return 0

    left, right, op = funcs[id]
    if determinate(left) != 0:
        return -1
    if determinate(right) != 0:
        return 1

    return 0

new_values = dict(values)
new_values['jgtb'] = eval('zfhn')

new_funcs = dict(funcs)
for id in funcs.keys():
    print("PASS", id)
    if id != 'humn':
        retval = determinate(id)
        if retval == -1:
            left, right, op = funcs[id]
            if op == add:
                new_funcs[left] = [id, right, sub]
            elif op == sub:
                new_funcs[left] = [id, right, add]
            elif op == mul:
                new_funcs[left] = [id, right, div]
            elif op == div:
                new_funcs[left] = [id, right, mul]
            
        if retval == 1:
            left, right, op = funcs[id]
            if op == add:
                new_funcs[right] = [id, left, sub]
            elif op == sub:
                new_funcs[right] = [left, id, sub]
            elif op == mul:
                new_funcs[right] = [id, left, div]
            elif op == div:
                new_funcs[right] = [left, id, div]

# funcs = new_funcs

def new_eval(id):
    if id in new_values:
        return new_values[id]
    left, right, op = new_funcs[id]

    val = op(new_eval(left), new_eval(right))
    # values[id] = val
    return val

# print(funcs['humn'])
ans = new_eval('wcdm') + new_eval('gdgb')
print(ans)

values['humn'] = ans
print(eval('jgtb'))
print(eval('zfhn'))
# funcs = {}
# values = {}

# def mul(x, y):
#     return x * y

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def div(x, y):
#     return x // y

# with open('21.txt', 'r') as file:
#     for line in file.readlines():
#         line = line[:-1]
#         tokens = line.split()

#         if len(tokens) == 2:
#             id, val = tokens
#             values[id[:-1]] = int(val)
#         elif len(tokens) == 4:
#             id, left, op, right = tokens
#             if op == '+':
#                 op = add
#             elif op == '-':
#                 op = sub
#             elif op == '*':
#                 op = mul
#             elif op == '/':
#                 op = div
            
#             funcs[id[:-1]] = [left, right, op]
                
#         else:
#             print("SOMETHING IS WRONG", line)
#             quit()

# def eval(id):
#     # if id == 'humn':
#         # return 1000000000000000
#     if id == 'root':
#         left, right, op = funcs[id]
#         return eval(left) == eval(right)

#     if id in answers:
#         return answers[id]
#     if id in values:
#         answers[id] = values[id]
#         return values[id]

#     left, right, op = funcs[id]

#     val = op(eval(left), eval(right))
#     answers[id] = val
#     return val

# answers = {}
# val = eval('zfhn')
# for i in range(-100, 0):
#     if i % 1000 == 0:
#         print("SEARCHING", i)

#     answers = {}
#     answers['humn'] = i
#     ans = eval('jgtb')
#     print(ans, val)
#     if eval('jgtb') == val:
#         print("HIT", i)
#         quit()
    
#     if i == 4482:
#         quit()
# # print(eval('root'))
    

