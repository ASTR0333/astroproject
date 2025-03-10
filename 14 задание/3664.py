def tox(n,x):
    s = ''
    while n!=0:
        last = n % x
        n =  n // x
        s = str(last) + s
    return s

k = 0
for x in range(2,11):
    ans = []
    s = tox(1755, x)
    for i in range(len(s)):
        if s[i] not in ans:
            ans.append(s[i])
    if len(ans) == len(s):
        k+=x
print(k)


