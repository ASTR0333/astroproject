file = open('j5.txt')
s = file.readline().strip()
k = 0
for i in range(len(s)-4):
    if s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4] != 'TOTOK' and s[i+2] + s[i+3] + s[i+4] == 'TOK':
        k+=1
print(k)