def is_four_digit(number):
    return 1000 <= abs(number) < 10000


def count_triples(numbers):
    n = len(numbers)
    count = 0
    max_sum = -float('inf')

    max_15 = max([x for x in numbers if str(x)[-2:] == '15'])

    for i in range(n - 2):
        x = numbers[i]
        y = numbers[i + 1]
        z = numbers[i + 2]
        if (is_four_digit(x) + is_four_digit(y) + is_four_digit(z) == 2) and (
                x % 7 == 0 or y % 7 == 0 or z % 7 == 0) and x + y + z > max_15:
            count += 1
            max_sum = max(max_sum, x + y + z)

    return count, max_sum


file = open('17-390.txt')
a = [int(s.strip()) for s in file]

count, min_sum = count_triples(a)

print(count,min_sum)