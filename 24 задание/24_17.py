with open('24_18284.txt') as file:
    s = file.readline().strip()

fl,fo,fv,fe=0,0,0,0
r,l=-1,0
ans = 10**10
while True:
    if not(fl>=1 and fo>=1 and fv>=1 and fe>=1):
        r+=1
        if r == len(s):
            break
        if s[r] == 'L':
            fl +=1
        if s[r] == 'O' and fl>=1:
            fo +=1
        if s[r] == 'V' and fl>=1 and fo >=1:
            fv +=1
        if s[r] == 'E' and fl>=1 and fo >=1 and fv>=1:
            fe +=1
    else:
        if s[l] == 'L':
            fl -=1
        l+=1
    if fl>=1 and fo>=1 and fv>=1 and fe>=1:
        ans = min(r-l+1,ans)

print(ans)



