with open('24_20909.txt') as file:
    s = file.readline().strip()

l,r=0,0
count_AB=0
ans = -10**10

while True:
    if count_AB<=100:
        r+=1
        if r == len(s):
            break
        if (r-l+1) >=2 and s[r-1] + s[r] == 'AB':
            count_AB+=1
    else:
        if s[l]+s[l+1]=='AB':
            count_AB-=1
        l+=1

    if count_AB == 100:
        ans = max(ans,r-l+1)

print(ans)