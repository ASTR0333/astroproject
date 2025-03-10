def to5(s):
    q = 0
    while s>0:
        if s%5==0:
            q+=1
        s = s // 5
    return q
ans=[]
for x in range(8300,30000):
    s = 5**100-x
    if to5(s) == 4:
        ans.append(x)
print(min(ans))
