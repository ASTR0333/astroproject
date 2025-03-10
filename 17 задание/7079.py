def dv(n):
    if str(abs(n))[0] == '6':
        return 1
    else:
        return 0


file = open('17-388.txt')
a = [int(s.strip()) for s in file]
print(a)
aos = [x for x in a if str(abs(x))[0] == '8']
os = max(aos)

ans = []
for i in range(len(a)-2):
    x = a[i]
    y = a[i + 1]
    z = a[i + 2]
    if dv(x) + dv(y) + dv(z) <=1:
        if x+y+z >= os:
            ans.append(x+y+z)
print(len(ans),min(ans))
