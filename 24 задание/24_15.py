

with open('24_19254.txt') as file:
    s = file.readline().strip()

r,l=-1,0
count_fsrq=0
ans = -10**10

while True:
    if count_fsrq <=80:
        r+=1
        if r == len(s):
            break
        if r-l+1>=4 and s[r-3] + s[r-2] + s[r-1] + s[r] == 'FSRQ':
            count_fsrq+=1
    else:
        if s[l] + s[l+1] + s[l+2] + s[l+3] == 'FSRQ' and r-l+1>=4:
            count_fsrq-=1
        l+=1

    if count_fsrq == 80:
        ans = max(ans,r-l+1)

print(ans )




