def is_five_digit(number):
    return 10000 <= abs(number) < 100000

def count_triples(numbers):
    n = len(numbers)
    count = 0
    min_sum = float('inf')
    average_13 = 0
    count_13 = 0
    for i in range(n):
        if str(numbers[i])[-2:] == '13':
            average_13 += numbers[i]
            count_13 += 1
    average_13 /= count_13

    for i in range(n - 2):
        x = numbers[i]
        y = numbers[i + 1]
        z = numbers[i + 2]
        if (is_five_digit(x) or is_five_digit(y) or is_five_digit(z)) and \
           (str(x)[-1] == '7') + (str(y)[-1] == '7') + (str(z)[-1] == '7') == 2 and \
           x > average_13 and y > average_13 and z > average_13:
            count += 1
            min_sum = min(min_sum, x + y + z)

    return count, min_sum

file = open('17-390.txt')
a = [int(s.strip()) for s in file]

count, min_sum = count_triples(a)

print(count,min_sum)