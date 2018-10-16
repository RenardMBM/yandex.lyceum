n = input()
try:
    n = float(n)

except ValueError:
    print('Incorrect Type')
    exit(0)

if n <= 1:
    print('NO')
    exit(0)

for divisor in range(2, int(n ** 0.5) + 1):
    if n % divisor == 0:
        print('NO')
        exit(0)

print('YES')
