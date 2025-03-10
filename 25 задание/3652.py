def mn(n):
    lst = []
    for d in range(2,int(n**0.5)+1):
        while n%d==0:
            lst.append(d)
            n//=d
    if n != 1:
        lst.append(n)
    lst.sort()
    return lst


ans = []
for x in range(106868,226868+1):
    lst = mn(x)
    lst1 = list(set(lst))
    if len(lst)==3 and len(lst1)==3:
        ans.append(x)
print(len(ans),max(ans))
