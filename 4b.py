ans = 0

with open('4.txt', 'r') as file:
    for line in file.readlines():
        line = line[:-1]
        r1, r2 = line.split(',')
        s1, e1 = r1.split('-')
        s2, e2 = r2.split('-')

        s1 = int(s1)
        s2 = int(s2)
        e1 = int(e1)
        e2 = int(e2)

        if s1 in range(s2, e2+1):
            ans += 1
        elif s2 in range(s1, e1+1):
            ans += 1
        elif e1 in range(s2, e2 + 1):
            ans += 1
        elif e2 in range(s1, e1 + 1):
            ans += 1

        print(s1, e1, s2, e2, ans)

print(ans)