with open('24.5_19717 (1).txt') as file:
    s = file.readline().strip()

r,l=-1,0
count_m=0
ans = -10**10

while True:
    if count_m<=278:
        r+=1
        if r == len(s):
            break
        if s[r] == 'M':
            count_m+=1
    else:
        if s[l]=='M':
            count_m-=1
        l+=1

    if count_m==278:
        ans = max(ans,r-l+1)

print(ans)
