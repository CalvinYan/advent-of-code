with open('6.txt', 'r') as file:
    line = file.readlines()[0][:-1]
    for i in range(len(line) - 3):
        letters = set(line[i:i+19])
        print(letters)
        if len(letters) == 4:
            print(i)
            quit()