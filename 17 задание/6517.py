ans = []
file = open('17-374.txt')
a = [int(s.strip()) for s in file]
aos = [x for x in a if x%2==0]
os = min(aos)
for i in range(len(a)-2):
    x = a[i]
    y = a[i+1]
    z = a[i+2]
    if (abs(x)%2==0 + abs(z)%2==0) == 1:
        if z%os == 0:
            ans.append(x+z)
print(len(ans),min(ans))