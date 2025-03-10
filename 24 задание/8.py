file = open('5.txt')
k = 0
s = file.readline().strip()
for i in range(len(s)):
    if s[i] == ')':
        k+=1
    if k == 1000:
        print(i+1)
        break