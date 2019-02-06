def sum1():

    n = input('Please enter your wanted number: ')
    count = 0

    for i in range(int(n)+1):
        count += 1
    print(count)

    return

def sum(n):

    total = 0

    for i in range(n):
        total = total + i + 1

    return total

num = int(input('Please enter your n: '))

print('The final sum is', sum(num))