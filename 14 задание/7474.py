def to3(s):
    q = 0
    while s>0:
        if s%3==0:
            q+=1
        s = s // 3
    return q
ans=[]
for x in range(1,2030):
    s = 3**100-x
    if to3(s) == 5:
        ans.append(x)
print(max(ans))
