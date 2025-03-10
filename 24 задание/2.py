file = open('j5.txt')
s = file.readline().strip()

k = 0
for i in range(len(s)-2):
    x,y,z = s[i],s[i+1],s[i+2]
    #if x+y+z == 'TTT':
        #k+=1
    if s[i:i+3] == 'TTT':
        k+=1

print(k)


