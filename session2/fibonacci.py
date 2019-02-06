a, b = 0, 1

n = int(input('Number of terms: '))

for i in range(n):
    print(a, end=' ')

    a, b = a, a+b
