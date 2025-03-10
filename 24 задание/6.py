file = open('j9.txt')
k = 0
s = file.readline().strip()
for i in range(len(s)-8):
    if s[i:i+8] == s[i:i+8][::-1]:
        k+=1
print(k)


