import numpy as np

sums = []

ans = 0
total = 0
with open('1.txt', 'r') as file:
    for line in file.readlines():
        if line[0] == '\n':
            sums.append(total)
            
            total = 0
        else:
            total += int(line[:-1])
        

sums = np.sort(sums)

print(np.sum(sums[-3:]))