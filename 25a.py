snafu = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
ufans = {0: '0', 1: '1', 2: '2', -1: '-', -2: '='}

total = 0 
with open('25.txt', 'r') as file:
    for line in file.readlines():
        number = line[:-1]
        for i, c in enumerate(number):
            power = len(number) - i - 1
            total += snafu[c] * (5 ** power)

print(total)

pow = 0

for pow in range(100):
    if 5 ** (pow + 1) > total:
        print("POWER IS", pow)
        break

def update(coeffs, pos, val):
    coeffs[pos] += val
    if coeffs[pos] > 2:
        coeffs[pos] -= 5
        update(coeffs, pos + 1, 1)

ans = ''
coeffs = [0 for _ in range(pow + 2)]
count = total
for p in range(pow + 2):
    mod = count % 5
    update(coeffs, p, mod)
    count //= 5

print([ufans[x] for x in coeffs[::-1]])
quit()
while pow >= 0:
    exp = 5 ** pow
    quotient = total // exp

    if pow > 2:
        coeffs[pow + 1] += 1
        coeffs[pow] -= (5 - quotient)
    else:
        coeffs[pow] += quotient
    
    remainder = total - exp * quotient
    # if remainder >=

    pow -= 1

    total -= quotient * exp

print([ufans[x] for x in coeffs])
