file = open('s1.txt')
lst = file.readlines()
lst = [x.strip() for x in lst ]

k = 0
for s in lst:
    if s.count('O')>s.count('C'):
        k+=1

print(k)

