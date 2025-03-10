file = open('331_24.txt')
s = file.readline().strip()

count_y=0
l=0
r=-1
ans=10**10

while True:
    if count_y<260:
        r+=1
        if r == len(s):
            break
        if s[r]=='Y':
            count_y+=1
    else:
        if s[l]=='Y':
            count_y-=1
        l+=1
    if count_y==260:
        ans=min(ans,(r-l+1))
print(ans)