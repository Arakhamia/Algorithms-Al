def max5(a, b, c, d, e):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    if d > largest:
        largest = d
    if e > largest:
        largest = e
    return largest

#if largest is "e"

# a > b > c > d
# მოხდება ორი მინიჭება, largest = a, largest = e

# a > b > c < d
# მოხდება სამი მინიჭება, largest = a, largest = d, largest = e

# a > b < c > d
# მოხდება სამი მინიჭება, largest = a, largest = c, largest = e

# a < b > c > d
# მოხდება სამი მინიჭება, largest = a, largest = b, largest = e

# a > b < c < d
# მოხდება ოთხი მინიჭება, largest = a, largest = c, largest = d, largest = e

# a < b > c < d
# მოხდება ოთხი მინიჭება, largest = a, largest = b, largest = d, largest = e

# a < b < c > d
# მოხდება ოთხი მინიჭება, largest = a, largest = b, largest = c, largest = e

# a < b < c < d
# მოხდება ხუთი მინიჭება, largest = a, largest = b, largest = c, largest = d, largest = e