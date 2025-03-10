def f(s):
    k = 0
    for i in range(len(s)-2):
        x, y = s[i], s[i + 2]
        if x == 'A' and y == 'B':
            k += 1
    return k



file = open('4.txt')
lst = [x.strip() for x in file.readlines()]




k2 = 0
for s in lst:
    if f(s) > 5:
        k2+=1
print(k2)


