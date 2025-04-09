def dict(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def ce(lst):
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
with open('27_B.txt') as file:
    for s in file:
        s = s.replace(',','.')
        x,y = [float(t) for t in s.split()]
        lst.append((x,y))

cl1=[]
cl2=[]
cl3=[]
cl4=[]

for x,y in lst:
    if y>10:
        if x < 15:
            cl1.append((x,y))
        else:
            cl2.append((x,y))
    else:
        if x > 15:
            cl4.append((x,y))
        else:
            cl3.append((x,y))

xcl1,ycl1=ce(cl1)
xcl2,ycl2=ce(cl2)
xcl3,ycl3=ce(cl3)
xcl4,ycl4=ce(cl4)

print((xcl1+xcl2+xcl3+xcl4)/4*10_000,(ycl1+ycl2+ycl3+ycl4)/4*10_000)