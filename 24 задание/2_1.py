file = open('301_24.txt')
s = file.readline().strip()

count_t = 0
l = 0
r = -1
ans = -10**10
while True:
    if count_t <=100:
        r += 1
        if r == len(s):
            break
        if s[r] == 'T':
            count_t+=1
    else:
        if s[l] == 'T':
            count_t-=1
        l+=1
    if count_t == 100:
        ans = max(ans,(r-l+1))
print(ans)

