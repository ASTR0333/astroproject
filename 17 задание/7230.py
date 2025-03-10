def is_four_digit(number):
    return 1000 <= abs(number) < 10000
def count_triples(numbers):

    n = len(numbers)
    count = 0
    min_sum = float('inf')

    average_28 = 0
    count_28 = 0
    for i in range(n):
        if str(numbers[i])[-2:] == '28':
            average_28 += numbers[i]
            count_28 += 1
    average_28 /= count_28

    for i in range(n - 2):
        x = numbers[i]
        y = numbers[i + 1]
        z = numbers[i + 2]
        if (is_four_digit(x) or is_four_digit(y) or is_four_digit(z)) and \
           (str(x)[-2:] == '11') + (str(y)[-2:] == '11') + (str(z)[-2:] == '11') == 2 and \
           x > average_28 and y > average_28 and z > average_28:
            count += 1
            min_sum = min(min_sum, x + y + z)

    return count, min_sum

file = open('17-390.txt')
a = [int(s.strip()) for s in file]

count, min_sum = count_triples(a)

print(count,min_sum)