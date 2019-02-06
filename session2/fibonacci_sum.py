a, b = 0, 1

counter = 0

n = int(input('Number of terms you want to be added up: '))

for i in range(n):
   a, b = b, a+b
   counter += a

print(counter)

