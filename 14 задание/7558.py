def to6(s):
    q = 0
    while s>0:
        if s%6==0:
            q+=1
    return q
ans = []
for x in range(0,2031):
    s = 6**2030 + 6**100 - x
    ans.append(to6(s))
print(max(ans))

