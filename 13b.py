import ast

ans = 0
packets = []
with open('13.txt', 'r') as file:
    lines = file.readlines()
    for i in range((len(lines) + 1) // 3):
        l1 = ast.literal_eval(lines[i*3][:-1])
        l2 = ast.literal_eval(lines[i*3 + 1][:-1])
        packets.append(l1)
        packets.append(l2)

        # print(l1)
        # print(l2)

# packets.append([[2]])
# packets.append([[6]])

print(len(packets))

def ordered(p1, p2):
    # print("CHECK", p1, p2)
    if not p1:
        if not p2: 
            # print('EH')
            return 0
        # print('NICE')
        return 1
    if not p2:
        # print('NOT NICE')
        return -1

    first1 = p1[0]
    first2 = p2[0]
    if isinstance(first1, list):
        if isinstance(first2, list):
            val = ordered(first1, first2)
            if val != 0:
                return val
        else:
            val = ordered(first1, [first2])
            if val != 0:
                return val
    elif isinstance(first2, list):
        val = ordered([first1], first2)
        if val != 0:
            return val
    else:
        if first1 > first2:
            # print('NOT NOICE')
            return -1
        elif first1 < first2: 
            # print('NOICE')
            return 1

    return ordered(p1[1:], p2[1:])

order = []

for p1 in packets:
    for i, p2 in enumerate(order):
        if ordered(p1, p2) >= 0:
            order.insert(i, p1)
            break
            
    order.append(p1)

ans = 1

for i, p in enumerate(order):
    if p == [[2]] or p == [[6]]:
        print(p)
        ans *= i + 1

print(ans)