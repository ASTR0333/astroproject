def is_symmetrical(n):

  return str(n) == str(n)[::-1]

def find_min_three_digit_number(numbers):
  min_three_digit_number = 1000
  for number in numbers:
    if number >= 100 and number < 1000 and is_symmetrical(number):
      min_three_digit_number = min(min_three_digit_number, number)
  return min_three_digit_number

def count_symmetrical_pairs(numbers, min_three_digit_number):

  n = len(numbers)
  count = 0
  min_sum = float('inf')
  for i in range(n // 2):
    if (numbers[i] * numbers[n - i - 1]) % min_three_digit_number == 0:
      count += 1
      min_sum = min(min_sum, numbers[i] + numbers[n - i - 1])
  return count, min_sum

with open('17-375.txt', 'r') as file:
  numbers = list(map(int, file.read().split()))

min_three_digit_number = find_min_three_digit_number(numbers)
count, min_sum = count_symmetrical_pairs(numbers, min_three_digit_number)

print(f"{count} {min_sum}")