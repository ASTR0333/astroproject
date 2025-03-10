ans = []
file = open('17.txt')
a = [int(s.strip()) for s in file]
aos = [x for x in a if abs(x)%10==3]
os = min(aos)
for i in range(len(a)-1):
    x,y = a[i],a[i+1]
    if abs(x)%10 == abs(y)%10:
        if ((abs(x)%3==0) + (abs(y)%3==0))==1:
            if (x**2 + y**2) <= os**2:
                ans.append(x**2 + y**2)
print(len(ans),max(ans))
