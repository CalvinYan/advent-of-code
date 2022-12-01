ans = 0
total = 0
with open('1.txt', 'r') as file:
    for line in file.readlines():
        if line[0] == '\n':
            if total > ans:
                ans = total
            
            total = 0
        else:
            total += int(line[:-1])
        


print(ans)