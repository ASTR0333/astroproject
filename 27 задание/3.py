def dict(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def cent(lst):
    mins = 10**10
    for x1,y1 in lst:
        s = 0
        for x2,y2 in lst:
            r = dict(x1,y1,x2,y2)
            s+=r
        if s < mins:
            mins = s
            x,y=x1,y1
    return x,y

lst = []
with open('27-3a.txt') as file:
    for s in file:
        s = s.replace(',','.')
        x,y = [float(t) for t in s.split()]
        lst.append((x,y))


cl1 = []
cl2 = []
for x,y in lst:
    if x>3:
        cl2.append((x,y))
    else:
        cl1.append((x,y))

xcl1,ycl1 = cent(cl1)
xcl2,ycl2 = cent(cl2)

print((xcl1+xcl2)/2*10_000,(ycl1+ycl2)/2*10_000)



