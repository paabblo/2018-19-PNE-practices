def count_a(seq):
    """Counting the number of A's in the sequence"""

    # Counter of A's
    result = 0

    for b in seq:
        if b == 'A':
            result += 1

    # Return the result
    return result


# Main program

s = input('Please enter the sequence: ')
na = count_a(s)
print("The number of As: {}".format(na))

# Calculate the total seq's length
tl = len(s)

# Calculate the percentage of A's in the seq
if tl > 0:
    perc = round(100.0 * na / tl, 1)
else:
    perc = 0

print('The total length is: {}'.format(tl))
print('The percentage of As is: {}%'.format(perc))