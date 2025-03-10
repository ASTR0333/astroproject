def mn(n):
    ans = []
    for d in range(2,int(n**0.5)+1):
        while n%d==0:
            ans.append(d)
            n//=d
    if n != 1:
        ans.append(n)
    ans.sort()
    return ans


for x in range(200800,200950+1):
    lst = mn(x)
    lst1 = list(set(lst))
    if len(lst) == 3 and len(lst1) == 3:
        if sum(lst1) < 1000:
            print(x,sum(lst1))