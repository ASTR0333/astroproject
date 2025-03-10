file = open('308_24.txt')
s = file.readline().strip()

count_w = 0
l = 0
r = -1
ans = -10**10

while True:
    if count_w <= 130:
        r+=1
        if r == len(s):
            break
        if s[r] == 'W':
            count_w +=1
    else:
        if s[l] == 'W':
            count_w -=1
        l+=1
    if count_w == 130:
        ans = max(ans,(r-l+1))
print(ans)