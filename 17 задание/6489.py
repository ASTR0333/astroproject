file = open('17-370.txt')
a = [int(s.strip()) for s in file]
aos = [x for x in a if (100 <= abs(x) < 1000) and (str(abs(x)) == str(abs(x))[::-1])]
os = min(aos)
ans = []
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if (1000 <= abs(x) < 10000) + (1000 <= abs(y) < 10000) == 1:
        if (x**2+y**2)%os == 0:
            ans.append(x**2+y**2)
print(len(ans),max(ans))
