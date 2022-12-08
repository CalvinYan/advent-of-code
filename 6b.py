with open('6.txt', 'r') as file:
    line = file.readlines()[0][:-1]
    for i in range(len(line) - 13):
        letters = set(line[i:i+14])
        print(letters)
        if len(letters) == 14:
            print(i)
            quit()