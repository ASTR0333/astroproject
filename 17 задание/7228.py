def is_three_digit(number):
    return 100 <= abs(number) < 1000

def count_triples(numbers):
    n = len(numbers)
    count = 0
    max_sum = -float('inf')

    average_38 = 0
    count_38 = 0
    for i in range(n):
        if str(numbers[i])[-2:] == '38':
            average_38 += numbers[i]
            count_38 += 1
    average_38 /= count_38

    for i in range(n - 2):
        x = numbers[i]
        y = numbers[i + 1]
        z = numbers[i + 2]
        if (is_three_digit(x) + is_three_digit(y) + is_three_digit(z)) >= 2 and \
           (str(x)[-1] == '3') + (str(y)[-1] == '3') + (str(z)[-1] == '3') == 1 and \
           x < average_38 and y < average_38 and z < average_38:
            count += 1
            max_sum = max(max_sum, x + y + z)  

    return count, max_sum

file = open('17-390.txt')
a = [int(s.strip()) for s in file]

count, min_sum = count_triples(a)

print(count,min_sum)