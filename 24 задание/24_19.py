from re import findall

with open('Задание 24.txt') as file:
    s = file.readline().strip()

# Исправленное регулярное выражение
pattern = r'(?:[FSWY]{3}|[FSWY]{2}|[FSWY]{1})?(?:FSWY)+(?:[FSWY]{3}|[FSWY]{2}|[FSWY]{1})?'

matches = findall(pattern, s)
matches.sort(key=len, reverse=True)

if matches:  # Проверка на случай, если совпадений не найдено
    print(len(matches[0]))
else:
    print("Совпадений не найдено")