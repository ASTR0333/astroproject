file = open('319_24.txt')
s = file.readline().strip()

count_z = 0
l = 0
r = -1
ans = 10**10

while True:
    if count_z < 200:
        r +=1
        if r == len(s):
            break
        if s[r] == 'Z':
            count_z+=1
    else:
        if s[l]=='Z':
            count_z-=1
        l+=1
    if count_z==200:
        ans=min(ans,(r-l+1))
print(ans)
