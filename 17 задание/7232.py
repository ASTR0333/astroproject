def is_five_digit(number):

    return 10000 <= abs(number) < 100000

def is_multiple_of(number, divisor):

    return number % divisor == 0

def count_triples(numbers):

    n = len(numbers)
    count = 0
    min_sum = float('inf')


    average_641 = 0
    count_641 = 0
    for i in range(n):
        if str(numbers[i])[-3:] == '641':
            average_641 += numbers[i]
            count_641 += 1
    average_641 /= count_641

    for i in range(n - 2):
        x = numbers[i]
        y = numbers[i + 1]
        z = numbers[i + 2]

        if (is_five_digit(x) or is_five_digit(y) or is_five_digit(z)) and \
           not (is_five_digit(x) and is_five_digit(y) and is_five_digit(z)) and \
           (is_multiple_of(x, 5) + is_multiple_of(y, 5) + is_multiple_of(z, 5)) > \
           (is_multiple_of(x, 11) + is_multiple_of(y, 11) + is_multiple_of(z, 11)) and \
           x > average_641 and y > average_641 and z > average_641:
            count += 1
            min_sum = min(min_sum, x + y + z)

    return count, min_sum

file = open('17-390.txt')
a = [int(s.strip()) for s in file]

count, min_sum = count_triples(a)

print(count,min_sum)