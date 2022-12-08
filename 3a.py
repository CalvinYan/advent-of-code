ans = 0

with open('3.txt') as file:
    for line in file.readlines():
        line = line[:-1]
        first, last = line[:len(line) // 2], line[len(line) // 2:]
        print(last, first)

        for i in last:
            if i in first:
                if i in 'abcdefghijklmnopqrstuvwxyz':
                    ans += ord(i) - 96
                elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    ans += ord(i) - 38
                else:
                    print("SOMETHING WRONG")
                print(i, ans)
                break
        

                
print(ans)