items = []
operation = []

test = []

monkeys = 8

activity = [0 for _ in range(monkeys)]
with open('11.txt', 'r') as file:
    lines = file.readlines()

    for i in range(monkeys):
        batch = [line[:-1] for line in lines[i * 7:i * 7 + 6]]
        items.append(list(map(int, batch[1][18:].split(','))))

        exec('fn = lambda old: ' + batch[2][19:])
        operation.append(fn)

        # Parse test
        factor = int(batch[3].split()[3])

        to_true = int(batch[4].split()[5])
        to_false = int(batch[5].split()[5])

        print(items[i], operation, factor, to_true, to_false)

        test.append((factor, to_true, to_false))


for round in range(20):
    for monkey in range(monkeys):
        for worry in items[monkey]:
            print("MONKEY:", monkey)
            print("WORRY:", worry)
            worry = operation[monkey](worry)
            print("FUNCTIONED:", worry)
            worry //= 3
            print("RELIEF:", worry)
            factor, to_true, to_false = test[monkey]

            to = to_true if worry % factor == 0 else to_false
            print("TO:", to)
            items[to].append(worry)

            activity[monkey] += 1

        items[monkey] = []

        print(items)

print(activity)
activity = sorted(activity)

print(activity[-2] * activity[-1])