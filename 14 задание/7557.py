def to6(s):
    q = 0
    while s>0:
        if s%6==0:
            q+=1
        s = s // 6
    return q
ans=[]
for x in range(1,2031):
    s = 6**260+6**160+6**60-x
    if to6(s) == 202:
        ans.append(x)
print(min(ans))


