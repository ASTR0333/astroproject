def f(x1,y1,x2,y2):
    if x1>x2 or y1>y2:
        return 0
    if x1==x2 and y1==y2:
        return 1
    return f(x1+1,y1,x2,y2) + f(x1*2,y1,x2,y2) + f(x1,y1+3,x2,y2)

print(f(1,0,17,27))