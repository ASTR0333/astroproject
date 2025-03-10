def to7(s):
    q = 0
    while s>0:
        if s%7==0:
            q+=1
        s = s // 7
    return q
ans=[]
for x in range(5000,20000):
    s = 7**100-x
    if to7(s) == 5:
        ans.append(x)
print(min(ans))
