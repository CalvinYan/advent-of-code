score = 0
with open('2.txt', 'r') as file:
    for line in file.readlines():
        you, me = line.split()
        print(you, me)

        you = ord(you) - 65

        if me is 'X':
            score += 0
            score += (you - 1) % 3 + 1
        elif me is 'Y':
            score += 3
            score += you + 1
        elif me is 'Z':
            score += 6
            score += (you + 1) % 3 + 1

        print(score)

print(score)
        