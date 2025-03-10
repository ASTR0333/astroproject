file = open('17-380.txt')
a = [int(s.strip()) for s in file]

aos = [x for x in a if abs(x)%100==25]
os = max(aos)

ans = []
for i in range(len(a)-2):
    x,y,z = a[i],a[i+1],a[i+2]
    if (len(str(abs(x))) == 4) + (len(str(abs(y))) == 4)  + (len(str(abs(z))) == 4)  <= 2:
        if x+y+z <= os:
            ans.append(x+y+z)

print(len(ans),max(ans))


