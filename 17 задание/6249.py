
file = open('17-366.txt')
a = [int(s.strip()) for s in file]

aos = [x for x in a if abs(x)%100==68]
os = min(aos)
ans = []
for i in range(len(a)-1):
    x,y = a[i], a[i+1]
    if (abs(x) % 100 == 68) + (abs(y) % 100 == 68)==1:
        if x**2 + y**2 >= os**2:
            ans.append(x**2 + y**2)
print(len(ans),max(ans))



