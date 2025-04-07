def dist(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def ce(lst):
    mins = 10**20
    for x1,y1 in lst:
        s = 0
        for x2,y2 in lst:
            r = dist(x1,y1,x2,y2)
            s+=r
        if s<mins:
            mins = s
            x,y=x1,y1
    return x,y

lst = []
with open('27-7b.txt') as file:
    for s in file:
        s = s.replace(',','.')
        x,y = [float(t) for t in s.split()]
        lst.append((x,y))

cl1=[]
cl2 = []
cl3 = []

for x,y in lst:
    if x>0:
        cl1.append((x,y))
    elif y>0:
        cl2.append((x, y))
    else:
        cl3.append((x, y))

xc1,yc1=ce(cl1)
xc2,yc2=ce(cl2)
xc3,yc3=ce(cl3)

print((xc1+xc2+xc3)/3*10000,(yc1+yc2+yc3)/3*10000)

