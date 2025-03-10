def dv(n):
    if 10 <= abs(n) < 100:
        return 1
    else:
        return 0


file = open('17-388.txt')
a = [int(s.strip()) for s in file]
print(a)
aos = [x for x in a if abs(x) % 100 == 68]
os = max(aos)

ans = []
for i in range(len(a)-3):
    x = a[i]
    y = a[i + 1]
    z = a[i + 2]
    w = a[i + 3]
    if dv(x) + dv(y) + dv(z) + dv(w) == 1 or dv(x) + dv(y) + dv(z) + dv(w) == 4:
        if x+y+z+w >= os:
            ans.append(x+y+z+w)
print(len(ans),max(ans))



