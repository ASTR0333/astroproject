
file = open('24-213.txt')
s = file.readline()

lst =[0]*len(s)

lst[0]=0
lst[1]=0
lst[2]=1
for i in range(3,len(s)):
    x,y,z = s[i-2],s[i-1],s[i]
    if x+y+z == 'NPO' or x+y+z == 'PNO':
        lst[i]= lst[i-3]+1
print(max(lst))



