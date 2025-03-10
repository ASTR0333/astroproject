def is_four_digit(number):

    return 1000 <= abs(number) < 10000

def is_multiple_of(number, divisor):

    return number % divisor == 0

def count_triples(numbers):

    n = len(numbers)
    count = 0
    min_sum = float('inf')


    average_615 = 0
    count_615 = 0
    for i in range(n):
        if str(numbers[i])[-3:] == '615':
            average_615 += numbers[i]
            count_615 += 1
    average_615 /= count_615

    for i in range(n - 2):
        x = numbers[i]
        y = numbers[i + 1]
        z = numbers[i + 2]
        # Проверяем условия для тройки (numbers[i], numbers[i + 1], numbers[i + 2])
        if (is_four_digit(x) or is_four_digit(y) or is_four_digit(z)) and \
           not (is_four_digit(x) and is_four_digit(y) and is_four_digit(z)) and \
           (is_multiple_of(x, 5) + is_multiple_of(y, 5) + is_multiple_of(z, 5)) > \
           (is_multiple_of(x, 7) + is_multiple_of(y, 7) + is_multiple_of(z, 7)) and \
           x > average_615 and y > average_615 and z > average_615:
            count += 1
            min_sum = min(min_sum, x + y + z)

    return count, min_sum

file = open('17-390.txt')
a = [int(s.strip()) for s in file]

count, min_sum = count_triples(a)

print(count,min_sum)