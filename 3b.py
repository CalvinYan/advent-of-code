
ans = 0

with open('3.txt') as file:
    lines = file.readlines()
    i = 0
    while i < len(lines):
        for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if c in lines[i] and c in lines[i+1] and c in lines[i+2]:
                if c in 'abcdefghijklmnopqrstuvwxyz':
                    ans += ord(c) - 96
                elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    ans += ord(c) - 38
                else:
                    print("SOMETHING WRONG")
                print(c, ans)
        i += 3
                
print(ans)