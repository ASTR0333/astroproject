def proverka(lst):
    if len(lst) >= 3:
        q = int(lst[0]) - int(lst[1])
        for i in range(len(lst)-1):
            if int(lst[i]) - int(lst[i+1]) == q:
                q = int(lst[i]) - int(lst[i+1])
            else:
                return 0
        return 1

    else:
        return 1



with open('24_18530.txt') as file:
    s = file.readline().strip()

lst = []

for i in range(len(s)):
    if s[i] in 'AE':
        lst.append(i)








