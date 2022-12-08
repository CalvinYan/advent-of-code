score = 0
with open('2.txt', 'r') as file:
    for line in file.readlines():
        you, me = line.split()
        print(you, me)

        you = ord(you) - 64
        me = ord(me) - 87

        score += me

        if you == me:
            score += 3
        elif (you - me) % 3 == 1:
            score += 0
        elif (me - you) % 3 == 1:
            score += 6

        print(score)

print(score)
        