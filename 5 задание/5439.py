ans = []
for i in range(1000,10000):
    n = i
    if n%2==0:
        n = sorted(list(str(n)),reverse = True)
        n = int(n[0] + n[1] + n[2] + n[3])
        r = n // 2
    else:
        n = sorted(list(str(n)))
        n = int(n[0] + n[1] + n[2] + n[3])
        r = n * 2

    if r-i==1:
        ans.append(r)
print(min(ans))

