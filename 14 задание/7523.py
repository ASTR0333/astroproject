def to7(s):
    q = 0
    while s>0:
        if s%7==0:
            q+=1
        s = s // 7
    return q
ans=[]
for x in range(1,2031):
    s = 7**91+7**160-x
    if to7(s) == 70:
        ans.append(x)
print(max(ans))

